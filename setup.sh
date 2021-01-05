mkdir -p ~/.streamlit/
echo "[general]
email = \"pratik.dr71@gmail.com\"
" > ~/.streamlit/credentials.toml
echo "[server]
headless = true
port = $PORT
enableCORS = false
" > ~/.streamlit/config.toml
