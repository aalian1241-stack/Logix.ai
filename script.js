document.getElementById('send-btn').addEventListener('click', processChat);
document.getElementById('user-input').addEventListener('keypress', function (e) {
    if (e.key === 'Enter') processChat();
});

function processChat() {
    const inputField = document.getElementById('user-input');
    const message = inputField.value.trim();
    
    if (message === "") return;

    addMessage(message, 'user-msg');
    inputField.value = "";

    // Simulate thinking time
    setTimeout(() => {
        const response = getBotAnswer(message);
        addMessage(response, 'bot-msg');
    }, 500);
}

function addMessage(text, className) {
    const chatWindow = document.getElementById('chat-window');
    const msgDiv = document.createElement('div');
    msgDiv.className = `msg ${className}`;
    msgDiv.innerText = text;
    chatWindow.appendChild(msgDiv);
    chatWindow.scrollTop = chatWindow.scrollHeight;
}

// TRAINING AREA: Add your Q&A here
function getBotAnswer(input) {
    const msg = input.toLowerCase();

    if (msg.includes("hello") || msg.includes("hi")) {
        return "Hello! How can I help you today?";
    } 
    
    if (msg.includes("time")) {
        return "The current time is " + new Date().toLocaleTimeString();
    }

    if (msg.includes("who created you")) {
        return "I am a Logix.ai bot created by you!";
    }

    if (msg.includes("weather")) {
        return "I can't check the sky yet, but it's always sunny in the code!";
    }

    // Default response if the bot doesn't know the answer
    return "That's a great question! I'm still learning, can you try asking something else?";
}
