import React from 'react'
import { AlertTriangle } from 'lucide-react'
// import Button from './components/common/Button.jsx'
import Button from './common/Button'

class ErrorBoundary extends React.Component {
  constructor(props) {
    super(props)
    this.state = { hasError: false, error: null, errorInfo: null }
  }

  static getDerivedStateFromError(error) {
    return { hasError: true }
  }

  componentDidCatch(error, errorInfo)
  {
console.error('Error caught by boundary:', error, errorInfo)
this.setState({ error, errorInfo })
}
render() {
if (this.state.hasError) {
return (
<div className="min-h-screen bg-gray-50 flex items-center justify-center p-4">
<div className="bg-white rounded-lg shadow-lg p-8 max-w-lg w-full text-center">
<AlertTriangle className="w-16 h-16 text-red-500 mx-auto mb-4" />
<h1 className="text-2xl font-bold text-gray-900 mb-2">
Oops! Something went wrong
</h1>
<p className="text-gray-600 mb-6">
We're sorry, but something unexpected happened. Please try refreshing the page.
</p>
<div className="space-y-3">
<Button
onClick={() => window.location.reload()}
fullWidth
>
Refresh Page
</Button>
<Button
variant="outline"
onClick={() => window.location.href = '/dashboard'}
fullWidth
>
Go to Dashboard
</Button>
</div>
{process.env.NODE_ENV === 'development' && this.state.error && (
<details className="mt-6 text-left">
<summary className="cursor-pointer text-sm text-gray-500 hover:text-gray-700">
Error Details (Development Only)
</summary>
<pre className="mt-2 text-xs bg-gray-100 p-4 rounded overflow-auto">
{this.state.error.toString()}
{this.state.errorInfo?.componentStack}
</pre>
</details>
)}
</div>
</div>
)
}
return this.props.children
}
}
export default ErrorBoundary