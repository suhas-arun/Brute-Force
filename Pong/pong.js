const canvas = document.getElementById("pong");
const ctx = canvas.getContext("2d");
const scoreLabel = document.getElementById("score");
const infoLabel = document.getElementById("info");

// difficulty refers to the speed of the AI paddle
const difficulty = 6;

const fps = 50;

const player = {
    x: 0,
    y: canvas.height / 2 - 50,
    width: 10,
    height: 100,
    colour: "#0f0",
    score: 0
};

const ai = {
    x: canvas.width - 10,
    y: canvas.height / 2 - 50,
    width: 10,
    height: 100,
    colour: "#0f0",
    score: 0,
    speed: difficulty,
};

const ball = {
    x: canvas.width / 2,
    y: canvas.height / 2,
    radius: 10,
    speed: 7,
    velocityX: 7,
    velocityY: 7,
    colour: "#f00"
};

let inPlay = false;

// function to draw a rectangle
function drawRect(x, y, width, height, colour) {
    ctx.fillStyle = colour;
    ctx.fillRect(x, y, width, height);
}

// function to draw a circle
function drawCircle(x, y, radius, colour) {
    ctx.fillStyle = colour;
    ctx.beginPath();
    ctx.arc(x, y, radius, 0, Math.PI * 2, false);
    ctx.closePath();
    ctx.fill();
}

// the player's paddle is controlled by the mouse
canvas.addEventListener("mousemove", movePaddle);

function movePaddle(event) {
    let rect = canvas.getBoundingClientRect();
    player.y = event.clientY - rect.top - player.height / 2;
    if (player.y + player.height > canvas.height) {
        player.y = canvas.height - player.height;
    }
    if (player.y < 0) {
        player.y = 0;
    }
}

function checkCollision(ball, paddle) {
    return (
        ball.x + ball.radius > paddle.x &&
        ball.y - ball.radius < paddle.y + paddle.height &&
        ball.x - ball.radius < paddle.x + paddle.width &&
        ball.y + ball.radius > paddle.y
    );
}

function resetBall() {
    ball.x = canvas.width / 2;
    ball.y = canvas.height / 2;
    ball.speed = 7;
    ball.velocityY = 7;
    ball.velocityX = -ball.velocityX;
    ball.velocityX = (ball.velocityX > 0) ? 7 : -7;
}

function render() {
    drawRect(0, 0, canvas.width, canvas.height, "#000");

    drawRect(player.x, player.y, player.width, player.height, player.colour);
    drawRect(ai.x, ai.y, ai.width, ai.height, ai.colour);
    drawCircle(ball.x, ball.y, ball.radius, ball.colour);

}

function resetGame() {
    player.score = 0;
    ai.score = 0
    ball.velocityX = 7;
    ball.velocityY = 7;
    clearInterval(window.refreshIntervalId)
}

function update() {
    if (!inPlay) {
        return
    }
    infoLabel.innerHTML = "Use the mouse to control the paddle"

    ball.x += ball.velocityX;
    ball.y += ball.velocityY;

    // update ai's position
    if (ball.y > ai.y) {
        ai.y += ai.speed
    }
    if (ball.y < ai.y + ai.height) {
        ai.y -= ai.speed
    }

    // the ball bounces off the walls
    if (ball.y + ball.radius > canvas.height || ball.y - ball.radius < 0) {
        ball.velocityY = -ball.velocityY;
    }

    let currentPlayer = (ball.x < canvas.width / 2) ? player : ai;

    if (checkCollision(ball, currentPlayer)) {
        let collisionPoint = (ball.y - (currentPlayer.y + currentPlayer.height / 2));
        collisionPoint = collisionPoint / (currentPlayer.height / 2);
        // pi/4 = 45 degrees
        let angle = (Math.PI / 4) * collisionPoint;

        let direction = (ball.x < canvas.width / 2) ? 1 : -1;

        ball.velocityX = direction * ball.speed * Math.cos(angle);
        ball.velocityY = direction * ball.speed * Math.sin(angle);

        // the ball speeds up each time it hits a paddle
        ball.speed += 0.5;

        // the computer's paddle speeds up over time
        ai.speed += 0.1
    }

    if (ball.x - ball.radius < 0) {
        ai.score++;
        resetBall();
        ai.speed =  difficulty
    } else
        if (ball.x + ball.radius > canvas.width) {
            player.score++;
            resetBall();
            ai.speed = difficulty
        }

    scoreLabel.innerHTML = `${player.score}    :    ${ai.score}`

    if (player.score == 5) {
        ball.velocityX = 0;
        ball.velocityY = 0;
        ball.x = canvas.width / 2
        ball.y = canvas.height / 2;
        render();
        inPlay = false;
        alert("You won! Well done!")
        resetGame();
        infoLabel.innerHTML = "Press enter to start the game";

    }
    if (ai.score == 5) {
        ball.velocityX = 0;
        ball.velocityY = 0;
        ball.x = canvas.width / 2
        ball.y = canvas.height / 2;
        render();
        inPlay = false;
        alert("Unlucky, you lost!");
        resetGame();
        infoLabel.innerHTML = "Press enter to start the game";

    }
}

render();

function game() {
    render();
    update();
}

addEventListener("keydown", event => {
    if ((event.code == "Enter" || event.code == "Return") && !inPlay) {
        inPlay = true;
        window.refreshIntervalId = setInterval(game, 1000 / fps)
    }
})