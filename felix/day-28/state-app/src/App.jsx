import { useState } from 'react'
import './App.css'
import Counter from './components/level1/Counter';
import ToggleMessage from './components/level1/ToggleMessage';
import InputMirror from './components/level1/InputMirror';
import ColorChanger from './components/level2/ColorChanger';
import CounterWithLimits from './components/level2/CounterWithLimits';
import VisibilityToggle from './components/level2/VisibilityToggle';
import TaskList from './components/Level3/TaskList';
import EmployeeManager from './components/level3/EmployeeManager';
import CheckboxList from "./components/level3/CheckboxList";

export default function App() {
  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-50 to-slate-100 p-8">
      <div className="max-w-6xl mx-auto">
        <h1 className="text-4xl font-bold text-slate-800 mb-2">React State Challenge Sheet</h1>
        
        {/* Level 1: Basic State */}
        <section className="mb-8">
          <h2 className="text-2xl font-semibold text-slate-700 mb-4 border-b-2 border-blue-500 pb-2">
            Level 1: Basic State
          </h2>
          <div className="grid gap-6 md:grid-cols-3">
            <Counter />
            <ToggleMessage />
            <InputMirror />
          </div>
        </section>

        {/* Level 2: Interactive State */}
        <section className="mb-8">
          <h2 className="text-2xl font-semibold text-slate-700 mb-4 border-b-2 border-green-500 pb-2">
            Level 2: Interactive State
          </h2>
          <div className="grid gap-6 md:grid-cols-3">
            <ColorChanger />
            <CounterWithLimits />
            <VisibilityToggle />
          </div>
        </section>

        {/* Level 3: Array/Object State */}
        <section>
          <h2 className="text-2xl font-semibold text-slate-700 mb-4 border-b-2 border-purple-500 pb-2">
            Level 3: Array/Object State
          </h2>
          <div className="grid gap-6 md:grid-cols-2">
            <TaskList />
            <EmployeeManager />
            <div className="md:col-span-2">
              <CheckboxList />
            </div>
          </div>
        </section>
      </div>
    </div>
  );
}