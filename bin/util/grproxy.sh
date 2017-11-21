# function install_grproxy
install_grproxy() {
    curl --silent --location http://lang.goodrain.me/public/grproxy -o /app/.heroku/grproxy
    chmod 755 /app/.heroku/grproxy
    cat > $BUILD_DIR/.profile.d/grproxy.sh <<EOF
    /app/.heroku/grproxy --logtostderr=false  --log_dir=/tmp --v=4  --bind-address=127.0.0.1 --master=172.30.42.1:8080 --namespace=\${TENANT_ID:-} --healthz-port=0   &
EOF
}
