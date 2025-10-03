import { useState, useEffect } from 'react'
import './App.css'

function App() {
  const [stats, setStats] = useState({
    total_packets: 0,
    threats_detected: 0,
    ml_threats: 0,
    ml_trained: false,
    status: 'connecting...'
  })

  const [threats, setThreats] = useState([])

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

    const fetchThreats = async () => {
      try {
        const response = await fetch('http://localhost:8000/api/threats')
        const data = await response.json()
        setThreats(data)
      } catch (error) {
        console.error('Threats not loaded:', error)
      }
    }

    fetchStats()
    fetchThreats()
    const interval = setInterval(() => {
      fetchStats()
      fetchThreats()
    }, 2000)
    return () => clearInterval(interval)
  }, [])

  return (
    <div className="bg-cyber-dark min-h-screen text-white p-8">
      {/* Header with ML Badge */}
      <div className="flex items-center justify-between mb-8">
        <h1 className="text-5xl font-bold text-cyber-blue">
          AI-NGFW Dashboard 🛡️
        </h1>
        {stats.ml_trained && (
          <div className="bg-purple-900 border-2 border-purple-500 rounded-lg px-6 py-3">
            <p className="text-purple-300 text-sm">🧠 ML Model Active</p>
            <p className="text-white font-bold text-2xl">{stats.ml_threats || 0} ML Threats</p>
          </div>
        )}
      </div>
      
      <div className="grid grid-cols-3 gap-6">
        {/* Total Packets Card */}
        <div className="bg-gray-800 p-6 rounded-lg border-2 border-cyan-500 hover:border-cyan-400 transition-all">
          <p className="text-gray-400 mb-2 text-sm uppercase tracking-wide">Total Packets</p>
          <p className="text-5xl font-bold text-cyan-400">{stats.total_packets.toLocaleString()}</p>
        </div>
        
        {/* Threats Detected Card - Animated when threats > 0 */}
        <div className={`bg-gray-800 p-6 rounded-lg border-2 transition-all ${
          stats.threats_detected > 0 
            ? 'border-red-500 animate-pulse' 
            : 'border-gray-600'
        }`}>
          <p className="text-gray-400 mb-2 text-sm uppercase tracking-wide">Threats Detected</p>
          <p className={`text-5xl font-bold ${
            stats.threats_detected > 0 ? 'text-red-500' : 'text-gray-500'
          }`}>
            {stats.threats_detected}
          </p>
          {stats.threats_detected > 0 && (
            <p className="text-red-400 text-xs mt-2 animate-pulse">⚠️ Active threats detected!</p>
          )}
        </div>
        
        {/* Status Card */}
        <div className="bg-gray-800 p-6 rounded-lg border-2 border-green-500 hover:border-green-400 transition-all">
          <p className="text-gray-400 mb-2 text-sm uppercase tracking-wide">System Status</p>
          <p className="text-3xl font-bold text-green-400 capitalize">{stats.status}</p>
          <div className="flex items-center mt-2">
            <div className="w-3 h-3 bg-green-500 rounded-full animate-pulse mr-2"></div>
            <span className="text-xs text-gray-400">Live monitoring active</span>
          </div>
        </div>
      </div>

      {/* Alert Banner - Shows when threats detected */}
      {stats.threats_detected > 0 && (
        <div className="mt-6 bg-red-900 border-2 border-red-500 rounded-lg p-4 animate-pulse">
          <div className="flex items-center">
            <span className="text-3xl mr-3">🚨</span>
            <div>
              <p className="text-xl font-bold text-red-300">Security Alert</p>
              <p className="text-red-200">{stats.threats_detected} suspicious packet(s) detected and blocked</p>
            </div>
          </div>
        </div>
      )}

      {/* Recent Threats Table */}
      {stats.threats_detected > 0 && (
        <div className="mt-6">
          <h2 className="text-2xl font-bold mb-4 text-red-400">🚨 Recent Threats</h2>
          <div className="bg-gray-800 rounded-lg overflow-hidden border-2 border-red-500">
            <table className="w-full text-left">
              <thead className="bg-gray-900 text-gray-400 uppercase text-xs">
                <tr>
                  <th className="p-4">Source IP</th>
                  <th className="p-4">Destination IP</th>
                  <th className="p-4">Port</th>
                  <th className="p-4">Type</th>
                  <th className="p-4">Size</th>
                  <th className="p-4">Detection Method</th>
                </tr>
              </thead>
              <tbody className="text-sm">
                {threats.length > 0 ? (
                  threats.slice(0, 10).map((threat, idx) => (
                    <tr key={idx} className="hover:bg-gray-700">
                      <td className="p-4 border-t border-gray-700 text-cyan-400">{threat.src_ip || 'N/A'}</td>
                      <td className="p-4 border-t border-gray-700 text-cyan-400">{threat.dst_ip || 'N/A'}</td>
                      <td className="p-4 border-t border-gray-700 text-red-400">{threat.dst_port || threat.src_port || 'N/A'}</td>
                      <td className="p-4 border-t border-gray-700">{threat.type || 'OTHER'}</td>
                      <td className="p-4 border-t border-gray-700">{threat.size} bytes</td>
                                            <td className="p-4 border-t border-gray-700">
                        <span className={`px-3 py-1 rounded-full text-xs font-bold uppercase tracking-wide ${
                          threat.detection_method === 'ML' 
                            ? 'bg-purple-600 text-white animate-pulse' 
                            : 'bg-orange-600 text-white'
                        }`}>
                          {threat.detection_method === 'ML' ? '🧠 ML' : '⚡ Rule'}
                        </span>
                      </td>
                    </tr>
                  ))
                ) : (
                  <tr>
                    <td className="p-4 border-t border-gray-700 text-center" colSpan="6">
                      No threats in recent packets
                    </td>
                  </tr>
                )}
              </tbody>
            </table>
          </div>
        </div>
      )}
    </div>
  )
}

export default App
