# UST Employee Task Management - Frontend

A modern, responsive frontend application for the UST Employee Task Management system built with React, TypeScript, and Tailwind CSS.

## Features

- 🎨 **Modern UI** - Beautiful, light-colored interface with smooth transitions
- 🔐 **Authentication** - Secure login with JWT token management
- 📊 **Dashboard** - Overview of tasks, employees, and statistics
- ✅ **Task Management** - Create, view, edit, and manage tasks with status tracking
- 👥 **Employee Management** - Manage employee information (Admin only)
- 👤 **User Management** - Manage user accounts and roles (Admin only)
- 💬 **Remarks** - Add comments and attachments to tasks
- 📱 **Responsive Design** - Works seamlessly on desktop and mobile devices
- ⚡ **Smooth Animations** - Fade-in, slide-up, and scale animations throughout

## Tech Stack

- **React 18** - UI library
- **TypeScript** - Type safety
- **Vite** - Build tool and dev server
- **Tailwind CSS** - Utility-first CSS framework
- **React Router** - Client-side routing
- **Axios** - HTTP client
- **Lucide React** - Icon library
- **date-fns** - Date formatting

## Getting Started

### Prerequisites

- Node.js 18+ and npm/yarn/pnpm
- Backend server running on `http://localhost:8000`

### Installation

1. Navigate to the frontend directory:
```bash
cd frontend
```

2. Install dependencies:
```bash
npm install
# or
yarn install
# or
pnpm install
```

3. Start the development server:
```bash
npm run dev
# or
yarn dev
# or
pnpm dev
```

4. Open your browser and navigate to `http://localhost:5173`

### Building for Production

```bash
npm run build
# or
yarn build
# or
pnpm build
```

The built files will be in the `dist` directory.

## Project Structure

```
frontend/
├── src/
│   ├── components/      # Reusable components
│   │   └── Layout.tsx   # Main layout with sidebar
│   ├── context/         # React context providers
│   │   └── AuthContext.tsx
│   ├── pages/           # Page components
│   │   ├── Login.tsx
│   │   ├── Dashboard.tsx
│   │   ├── Tasks.tsx
│   │   ├── TaskDetail.tsx
│   │   ├── Employees.tsx
│   │   └── Users.tsx
│   ├── services/        # API service layer
│   │   └── api.ts
│   ├── types/           # TypeScript type definitions
│   │   └── index.ts
│   ├── App.tsx          # Main app component
│   ├── main.tsx         # Entry point
│   └── index.css        # Global styles
├── index.html
├── package.json
├── tsconfig.json
├── vite.config.ts
└── tailwind.config.js
```

## Features in Detail

### Authentication
- Login with Employee ID and password
- JWT token stored in localStorage
- Protected routes with authentication check
- Auto-redirect to login if not authenticated

### Dashboard
- Overview cards showing task statistics
- Recent tasks list
- Quick stats and completion rates
- Smooth animations on load

### Task Management
- View all tasks with filtering by status and priority
- Search tasks by title or description
- Create new tasks with full details
- View task details with remarks
- Update task status and priority
- Delete tasks (Admin only)

### Employee Management
- View all employees in a table
- Create new employees (Admin only)
- Edit employee information (Admin only)
- Delete employees (Admin only)
- Search employees by name, email, or designation

### User Management
- View all users with roles and status
- Create new users (Admin only)
- Edit user roles and status (Admin only)
- Delete users (Admin only)
- Search users by ID, role, or status

### Remarks/Comments
- Add remarks to tasks with optional file attachments
- View all remarks for a task
- Real-time updates

## Color Scheme

The application uses a light, modern color palette:
- **Primary**: Blue shades (primary-50 to primary-900)
- **Background**: Gradient from blue-50 via white to purple-50
- **Cards**: White with subtle borders and shadows
- **Status Colors**: 
  - Green for completed/done
  - Yellow for in-progress
  - Orange for pending/to-do
  - Red for high priority

## Animations

The application includes smooth transitions:
- **Fade-in**: Page transitions
- **Slide-up**: List items and cards
- **Scale-in**: Modal dialogs
- **Hover effects**: Interactive elements

## API Integration

The frontend communicates with the backend API at `http://localhost:8000`. All API calls are handled through the `api.ts` service file, which includes:
- Automatic token injection
- Error handling
- Type-safe request/response handling

## Browser Support

- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)

## License

This project is part of the UST Employee Task Management system.


