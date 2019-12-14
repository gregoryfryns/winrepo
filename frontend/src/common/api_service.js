import { CSRF_TOKEN } from './csrf_token';

async function getJSON(response) {
  if (response.status === 204) {
    return '';
  } else if (response.status === 404) {
    return null;
  } else {
    return response.json();
  }
}

function apiService(endpoint, method, data) {
  const config = {
    method: method || 'GET',
    body: data !== undefined ? JSON.stringify(data) : null,
    headers: {
      'content-type': 'application/json',
      'x-CSRFTOKEN': CSRF_TOKEN
    }
  };

  return fetch(endpoint, config)
    .then(getJSON)
    .catch(error => console.log(error));
}

export { apiService };
