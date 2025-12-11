module.exports = {
    devServer: {
        port: 5000,
        proxy: "http://172.16.0.203/sso_login/"
    }
}