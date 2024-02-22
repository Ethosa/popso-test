import axios from "axios"
const API_URL = "http://127.0.0.1:8000"


async function makePostRequest(url) {
  let apiRes = null
  try {
    apiRes = await axios.post(url)
    apiRes = apiRes.data
  } catch (err) {
    apiRes = err.response.data
  }
  return apiRes
}


async function makeGetRequest(url) {
  let apiRes = null
  try {
    apiRes = await axios.get(url)
    apiRes = apiRes.data
  } catch (err) {
    apiRes = err.response.data
  }
  return apiRes
}


async function auth(login, password) {
  return await makePostRequest(`${API_URL}/auth/?login=${login}&password=${password}`)
}


async function register(login, password) {
  return await makePostRequest(`${API_URL}/register/?login=${login}&password=${password}`)
}


async function getById(userId) {
  return await makeGetRequest(`${API_URL}/user/${userId}`)
}

async function updateUser(oldLogin, oldPassword, firstName = null, lastName = null, login = null, password = null) {
  let queries = []
  if (firstName)
    queries.push(`first_name=${firstName}`)
  if (lastName)
    queries.push(`last_name=${lastName}`)
  if (login)
    queries.push(`login=${login}`)
  if (password)
    queries.push(`password=${password}`)
  return await makePostRequest(
    `${API_URL}/update-user/?oldLogin=${oldLogin}&oldPassword=${oldPassword}&${queries.join("&")}`
  )
}


export default {
  auth: auth,
  register: register,
  updateUser: updateUser,
  getById: getById,
}