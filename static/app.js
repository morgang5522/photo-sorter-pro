function assign(setName) {
  const sidebar = document.getElementById("sets-sidebar");
  if (sidebar) {
    localStorage.setItem("sidebarScroll", sidebar.scrollTop);
  }

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

document.addEventListener("DOMContentLoaded", () => {
  const scrollPos = localStorage.getItem("sidebarScroll");
  if (scrollPos) {
    const sidebar = document.getElementById("sets-sidebar");
    if (sidebar) {
      sidebar.scrollTop = scrollPos;
    }
    localStorage.removeItem("sidebarScroll");
  }
});

document.addEventListener("keydown", (e) => {
  if (e.key === "n") newSet();
});

