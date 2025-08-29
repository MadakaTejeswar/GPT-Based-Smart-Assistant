src/components/Home/index.js
import {Component} from 'react'
import Message from '../Message'
import Login from '../Login'
import Logout from '../Logout'
import './index.css'

class Home extends Component {
  state = {isLoggedIn: false}

  onLogin = () => {
    this.setState({isLoggedIn: true})
  }

  onLogout = () => {
    this.setState({isLoggedIn: false})
  }

  render() {
    const {isLoggedIn} = this.state
    return (
      <div className="home-container">
        <div className="card-container">
          <Message isLoggedIn={isLoggedIn} />
          {isLoggedIn ? (
            <Logout onLogout={this.onLogout} />
          ) : (
            <Login onLogin={this.onLogin} />
          )}
        </div>
      </div>
    )
  }
}

export default Home

src/components/Home/index.css
.home-container {
  background-color: #f8fafc;
  height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
}

.card-container {
  background: linear-gradient(to bottom, #2b2c49, #b5b9ff);
  border-radius: 12px;
  padding: 30px;
  text-align: center;
}

src/components/Message/index.js
import './index.css'

const Message = props => {
  const {isLoggedIn} = props
  return (
    <h1 className="message">
      {isLoggedIn ? 'Welcome User' : 'Please Login'}
    </h1>
  )
}

export default Message

src/components/Message/index.css
.message {
  font-family: 'Roboto';
  font-size: 22px;
  font-weight: bold;
  color: #ffffff;
  margin-bottom: 20px;
}

src/components/Login/index.js
import './index.css'

const Login = props => {
  const {onLogin} = props
  return (
    <button className="btn" type="button" onClick={onLogin}>
      Login
    </button>
  )
}

export default Login

src/components/Login/index.css
.btn {
  background-color: #ffffff;
  color: #303150;
  border: none;
  border-radius: 6px;
  padding: 8px 16px;
  font-size: 14px;
  cursor: pointer;
}

src/components/Logout/index.js
import './index.css'

const Logout = props => {
  const {onLogout} = props
  return (
    <button className="btn" type="button" onClick={onLogout}>
      Logout
    </button>
  )
}

export default Logout

src/components/Logout/index.css
.btn {
  background-color: #ffffff;
  color: #303150;
  border: none;
  border-radius: 6px;
  padding: 8px 16px;
  font-size: 14px;
  cursor: pointer;
}

src/App.js
import Home from './components/Home'

const App = () => <Home />

export default App
