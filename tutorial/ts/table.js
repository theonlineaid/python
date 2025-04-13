const url = `https://jsonplaceholder.typicode.com/posts`

async function fetchData(url) {
    const response = await fetch(url);
    const data = await response.json();
    return data;
}

const result = await fetchData(url);
console.table(result, ["id", "title"]);