export let theme = "light";

export function toggleTheme(){
    return theme = theme === "light" ? "dark" : "light";
}