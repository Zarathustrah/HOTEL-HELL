import React from 'react'

const App = () => {
  React.useEffect(() => {
    const getData = async () => {
      const res = await fetch('/api/places')
      const data = await res.json()
      console.log(data)
    }
    getData()
  }, [])
 
  return (
    <h1>Hello World</h1>
  )
}
export default App