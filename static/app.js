function assign(setName) {
  fetch("/assign", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      image: document.querySelector("#current-image-name").textContent.trim(),
      set: setName,
    }),
  }).then(() => location.reload());
}

function newSet() {
  const name = prompt("Enter a name for the new set (optional):");
  if (name === null) return;
  assign(name);
}

document.addEventListener("keydown", (e) => {
  if (e.key === "n") newSet();
});
