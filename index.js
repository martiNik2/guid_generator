async function fetchGuid() {
  const response = await fetch("http://127.0.0.1:8000/");
  const data = await response.json();
  return data;
}

const generateButton = document.querySelector(".generate");
const guidDiv = document.querySelector(".guid");

generateButton.addEventListener("click", async () => {
  const guid = fetchGuid().then((data) => data.guid);
  guidDiv.textContent = await guid;
});
