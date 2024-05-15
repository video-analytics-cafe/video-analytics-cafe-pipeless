PORT=9092

# Kill any process using port 5000
#PID=$(lsof -ti:$PORT)
#if [ ! -z "$PID" ]; then
#  echo "kill $PID on port $PORT"
#  kill  $PID
#fi


#NGROK_PID=$(pgrep ngrok)
#if [ ! -z "$NGROK_PID" ]; then
#  echo "Killing existing ngrok processes: $NGROK_PID..."
#  kill  $NGROK_PID
#fi

# Wait a bit to ensure the processes have been terminated
sleep 2

# run ngrok in the background
nohup ngrok http $PORT --response-header-add "Access-Control-Allow-Origin: *" --log=stdout > log_ngrok_pipeless.log 2>&1&

sleep 4

# get the public url
PUBLIC_URL=$(curl -sS http://localhost:4040/api/tunnels | jq -r '.tunnels[0].public_url')
echo "Ngrok url: " $PUBLIC_URL