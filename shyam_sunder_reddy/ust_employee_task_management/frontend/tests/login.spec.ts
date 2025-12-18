import { test, expect } from "@playwright/test";

// This test attempts to open the frontend on ports 5173 or 5174,
// fills the login form, clicks Sign In and captures the /auth/login
// request + response and checks that a token is stored in localStorage.

const PORTS = [5173, 5174];

test("login flow - captures /auth/login and token storage", async ({
  page,
}) => {
  page.on("console", (msg) => console.log("PAGE LOG:", msg.type(), msg.text()));

  let opened = false;
  let base = "";
  for (const p of PORTS) {
    const url = `http://localhost:${p}`;
    try {
      const resp = await page.goto(url, {
        waitUntil: "domcontentloaded",
        timeout: 5000,
      });
      // If navigation succeeded (status 200 or no status for file loads), proceed
      if (resp && (resp.status() === 200 || resp.status() === 304)) {
        opened = true;
        base = url;
        break;
      }
      // resp can be null for some SPA frontends; consider success if no exception
      if (!resp) {
        opened = true;
        base = url;
        break;
      }
    } catch (e) {
      // try next port
    }
  }

  expect(opened).toBeTruthy();

  // Wait for the login form elements
  await page.waitForSelector("#e_id", { timeout: 5000 });
  await page.waitForSelector("#password", { timeout: 5000 });

  // Fill credentials
  await page.fill("#e_id", "1");
  await page.fill("#password", "password123");

  // Intercept the response for /auth/login
  const [response] = await Promise.all([
    page.waitForResponse(
      (resp) => resp.url().includes("/auth/login") && resp.status() === 200,
      { timeout: 5000 }
    ),
    page.click("button[type=submit]"),
  ]);

  expect(response).toBeTruthy();
  const body = await response.json();
  console.log("AUTH RESPONSE:", JSON.stringify(body));

  expect(body).toHaveProperty("access_token");
  expect(body).toHaveProperty("user");

  // Wait for token to be set in localStorage by the app
  await page.waitForFunction(() => !!localStorage.getItem("token"), null, {
    timeout: 5000,
  });
  const token = await page.evaluate(() => localStorage.getItem("token"));
  console.log("LOCALSTORAGE token:", token);
  expect(token).toBeTruthy();
});
