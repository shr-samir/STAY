import { BrowserRouter, Routes, Route } from 'react-router-dom'
import Home from './pages/Home'
import About from './pages/About'
import Profile from './pages/Profile'
import SignIn from './pages/Signin'
import SignOut from './pages/SignOut'
import Header from './components/Header'

const App = () => {
  return (
    <BrowserRouter>
      <Header />
      <Routes>
        <Route path='/' element={<Home /> }></Route>
        <Route path='/about' element={<About />}></Route>
        <Route path='/profile' element={<Profile />}></Route>
        <Route path='/sign-in' element={<SignIn />}></Route>
        <Route path='/sign-out' element={<SignOut />}></Route>
      </Routes>
    </BrowserRouter>
  )
}

export default App