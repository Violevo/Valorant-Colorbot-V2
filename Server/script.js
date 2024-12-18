// Generate and animate stars
function createStars() {
    const numStars = 200; // Number of stars to create
    const container = document.getElementById('stars-container');
    
    for (let i = 0; i < numStars; i++) {
        const star = document.createElement('div');
        star.classList.add('star');
        
        // Random position across the larger container
        const x = Math.random() * 100 + 'vw'; // Random x position (now based on vw)
        const y = Math.random() * 100 + 'vh'; // Random y position (now based on vh)
        star.style.left = x;
        star.style.top = y;
        
        // Keep the size of stars consistent (1px to 3px)
        const size = Math.random() * 3 + 1;  // Random size between 1px and 4px
        star.style.width = size + 'px';
        star.style.height = size + 'px';
        
        // Random animation duration (2s to 5s)
        const duration = Math.random() * 3 + 2;
        star.style.animationDuration = duration + 's';
        
        // Random delay for the twinkle effect (up to 5s)
        const delay = Math.random() * 5;
        star.style.animationDelay = delay + 's';
        
        container.appendChild(star);
    }
}

// Animate the movement of the stars inside the large container
function moveStars() {
    const container = document.getElementById('stars-container');
    const stars = container.querySelectorAll('.star');
    
    const radius = 10; // Fixed radius for all stars to move in the same path
    const speed = 0.0001; // Slow and smooth movement speed

    // Create a base angle for the synchronized movement
    let angle = 0;

    stars.forEach((star, index) => {
        // Give each star a random offset to start at a different position on the path
        const offsetAngle = (Math.random() * 360); // Random offset for each star's starting position
        let currentAngle = offsetAngle;

        function updatePosition() {
            // Increment angle for smooth movement
            angle += speed;

            // Update each star's position based on its offset and current angle
            currentAngle = angle + offsetAngle;  // Synchronized movement with individual offset

            // Calculate the new position
            const xOffset = Math.cos(currentAngle) * radius;
            const yOffset = Math.sin(currentAngle) * radius;

            // Apply the transformation to move the star
            star.style.transform = `translate(${xOffset}px, ${yOffset}px)`;

            requestAnimationFrame(updatePosition); // Continue the animation for the next frame
        }

        updatePosition(); // Start the movement for each star
    });
}

window.onload = function() {
    createStars();  // Generate the stars
    moveStars();    // Animate the stars' movement
    loadSettings();
}

const colorToleranceSlider = document.getElementById('colorTolerance');
const colorToleranceValue = document.getElementById('colorToleranceValue');

// Update the label dynamically based on the slider value
colorToleranceSlider.addEventListener('input', () => {
    colorToleranceValue.textContent = colorToleranceSlider.value;
});

const triggerDelaySlider = document.getElementById('triggerDelay');
const triggerDelayValue = document.getElementById('triggerDelayValue');

// Update the label dynamically based on the slider value
triggerDelaySlider.addEventListener('input', () => {
    triggerDelayValue.textContent = triggerDelaySlider.value;
});

let socket; // To hold the WebSocket connection
let sendInterval; // To hold the interval ID

// Function to update the settings in the UI
function updateSettings(settings) {
    // Update Resolution
    if (settings.resolution) {
        document.getElementById('resolution').value = settings.resolution;
    }

    // Update Enemy Color
    if (settings.enemyColor) {
        const enemyColorSelect = document.getElementById('enemyColor');
        for (let i = 0; i < enemyColorSelect.options.length; i++) {
            if (enemyColorSelect.options[i].value === settings.enemyColor) {
                enemyColorSelect.selectedIndex = i;
                break;
            }
        }
    }

    // Update Trigger Area
    if (settings.triggerArea !== undefined) {
        document.getElementById('triggerArea').value = settings.triggerArea;
    }

    // Update Trigger Delay
    if (settings.triggerDelay !== undefined) {
        const triggerDelayInput = document.getElementById('triggerDelay');
        const triggerDelayValueLabel = document.getElementById('triggerDelayValue');
        triggerDelayInput.value = settings.triggerDelay;
        triggerDelayValueLabel.textContent = settings.triggerDelay;
    }

    // Update Color Tolerance
    if (settings.colorTolerance !== undefined) {
        const colorToleranceInput = document.getElementById('colorTolerance');
        const colorToleranceValueLabel = document.getElementById('colorToleranceValue');
        colorToleranceInput.value = settings.colorTolerance;
        colorToleranceValueLabel.textContent = settings.colorTolerance;
    }
}

// Function to save the settings to localStorage and update the UI
function saveSettings() {
    // Get the values from the form
    const resolution = document.getElementById("resolution").value;
    const enemyColor = document.getElementById("enemyColor").value;
    const triggerArea = document.getElementById("triggerArea").value; 
    const triggerDelay = document.getElementById("triggerDelay").value;
    const colorTolerance = document.getElementById("colorTolerance").value;

    // Create an object to store the settings
    const settings = {
        resolution: resolution,
        enemyColor: enemyColor,
        triggerArea: triggerArea,
        triggerDelay: triggerDelay,
        colorTolerance: colorTolerance
    };

    // Create a WebSocket connection to the Raspberry Pi server
    const socket = new WebSocket('ws://<raspberry-pi-ip>:<port>');  // Replace with Raspberry Pi IP and port
    console.log("Socket Opened...");

    socket.onopen = () => {
        console.log("Found Device!");

        // Send the settings object once
        socket.send(JSON.stringify(settings));
        console.log("Sent settings:", settings);

        // Close the socket after sending
        socket.close();
        console.log("Closing connection...");
    };

    // Save settings to localStorage
    localStorage.setItem('gameSettings', JSON.stringify(settings));

    // Update the UI with the current settings
    updateSettings(settings);
}

// Function to load settings from localStorage
function loadSettings() {
    const savedSettings = localStorage.getItem('gameSettings');
    if (savedSettings) {
        updateSettings(JSON.parse(savedSettings));
    }
}



