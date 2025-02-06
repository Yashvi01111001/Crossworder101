const gridData = [
    ['C', 'A', 'T', 'L', 'P', 'X', 'S', 'U', 'N', 'D'],
    ['M', 'O', 'R', 'E', 'Z', 'Q', 'A', 'B', 'A', 'V'],
    ['D', 'O', 'G', 'S', 'N', 'T', 'R', 'E', 'E', 'K'],
    ['J', 'H', 'A', 'W', 'U', 'I', 'M', 'X', 'E', 'Y'],
    ['V', 'F', 'T', 'C', 'O', 'G', 'P', 'H', 'A', 'T'],
    ['Y', 'B', 'O', 'O', 'K', 'S', 'R', 'U', 'I', 'W'],
    ['U', 'N', 'A', 'B', 'Y', 'H', 'O', 'U', 'S', 'E'],
    ['B', 'I', 'R', 'D', 'T', 'L', 'N', 'O', 'N', 'C'],
    ['X', 'W', 'N', 'O', 'M', 'A', 'P', 'R', 'D', 'J'],
    ['Q', 'G', 'K', 'I', 'T', 'E', 'F', 'L', 'O', 'S']
];

// Render Grid
function createGrid() {
    let grid = document.getElementById('grid');
    grid.innerHTML = '';
    gridData.forEach(row => {
        row.forEach(letter => {
            let cell = document.createElement('div');
            cell.className = 'cell';
            cell.innerText = letter;
            grid.appendChild(cell);
        });
    });
}

// AJAX Request to Python Backend
function findWord() {
    let word = document.getElementById("wordInput").value;
    fetch("https://your-backend-url.com/find", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ word })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("results").innerHTML = 
            `<p>Found: ${data.word} at positions: ${JSON.stringify(data.positions)}</p>`;
    });
}

// Initialize Grid
createGrid();