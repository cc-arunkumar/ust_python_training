import React from 'react'

const Card = ({ children, className = '', padding = true, hover = false }) => {
  return (
    <div 
      className={`
        bg-white rounded-lg shadow border border-gray-200
        ${padding ? 'p-6' : ''}
        ${hover ? 'hover:shadow-lg transition-shadow' : ''}
        ${className}
      `}
    >
      {children}
    </div>
  )
}

export default Card