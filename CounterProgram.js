const decreaseButton = document.getElementById("decrease");
const increaseButton = document.getElementById("increase");
const resetButton = document.getElementById("reset");
const counterDisplay = document.getElementById("Counter");

let count = 0; // Counter starts at 0

// Decrease button functionality
decreaseButton.onclick = () => {
    count--;
    counterDisplay.textContent = count; // Update displayed count
};

// Increase button functionality
increaseButton.onclick = () => {
    count++;
    counterDisplay.textContent = count; // Update displayed count
};

// Reset button functionality
resetButton.onclick = () => {
    count = 0; // Reset count to 0
    counterDisplay.textContent = count; // Update displayed count
};
