import React from 'react'
import { Loader2 } from 'lucide-react'

const LoadingSpinner = ({ size = 'default', fullScreen = false, text = 'Loading...' }) => {
  const sizeClasses = {
    small: 'w-4 h-4',
    default: 'w-8 h-8',
    large: 'w-12 h-12',
  }

  if (fullScreen) {
    return (
      <div className="fixed inset-0 flex items-center justify-center bg-white bg-opacity-75 z-50">
        <div className="text-center">
          <Loader2 className={`${sizeClasses.large} animate-spin text-primary-600 mx-auto`} />
          <p className="mt-4 text-gray-600">{text}</p>
        </div>
      </div>
    )
  }

  return (
    <div className="flex items-center justify-center p-4">
      <Loader2 className={`${sizeClasses[size]} animate-spin text-primary-600`} />
      {text && <span className="ml-2 text-gray-600">{text}</span>}
    </div>
  )
}

export default LoadingSpinner