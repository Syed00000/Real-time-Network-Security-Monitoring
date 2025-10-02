import { useState, useEffect } from 'react'
import './App.css'

function App() {
  const [stats, setStats] = useState({
    total_packets: 0,
    threats_detected: 0,
    status: 'connecting...'
  })

  useEffect(() => {
    // Fetch data from backend every 2 seconds
    const fetchStats = async () => {
      try {
        const response = await fetch('http://localhost:8000/api/stats')
        const data = await response.json()
        setStats(data)
      } catch (error) {
        console.error('Backend not connected:', error)
      }
    }

    fetchStats()
    const interval = setInterval(fetchStats, 2000)
    return () => clearInterval(interval)
  }, [])

  return (
    <div className="bg-cyber-dark min-h-screen text-white p-8">
      <h1 className="text-5xl font-bold mb-8 text-cyber-blue">
        AI-NGFW Dashboard 🛡️
      </h1>
      
      <div className="grid grid-cols-3 gap-6">
        <div className="bg-gray-800 p-6 rounded-lg border border-cyber-blue">
          <p className="text-gray-400 mb-2">Total Packets</p>
          <p className="text-4xl font-bold">{stats.total_packets}</p>
        </div>
        
        <div className="bg-gray-800 p-6 rounded-lg border border-red-500">
          <p className="text-gray-400 mb-2">Threats Detected</p>
          <p className="text-4xl font-bold text-red-500">{stats.threats_detected}</p>
        </div>
        
        <div className="bg-gray-800 p-6 rounded-lg border border-green-500">
          <p className="text-gray-400 mb-2">Status</p>
          <p className="text-2xl font-bold text-green-400">{stats.status}</p>
        </div>
      </div>
    </div>
  )
}

export default App
