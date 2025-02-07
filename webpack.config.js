const path = require('path');

module.exports ={
    mode: 'development',
    entry: './assets/scripts/index.js',
    output: {
        // publicPath:'http://127.0.0.1:8080/',
        // path: path.resolve(__dirname, 'homePage', 'static'),
        path: path.resolve(__dirname, 'assets', 'js'),
        filename: 'bundle.js'
    },
    module:{
        rules: [
            {
                test: /\.(?:js|mjs|cjs)$/,
                exclude: /node_modules/,
                use: {
                  loader: 'babel-loader',
                  options: {
                    targets: "defaults",
                    presets: [
                      ['@babel/preset-env']
                    ]
                  }
                }
              },
            {
                test: /\.(css)$/,
                use: ['style-loader','css-loader'],
            }
        ]
    },
    devServer: {
        host: '127.0.0.1',
        port: '8080',
        // allowedHosts: ['http://127.0.0.1:8000'],
        headers: {
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "GET, POST, PUT, DELETE, PATCH, OPTIONS",
            "Access-Control-Allow-Headers": "X-Requested-With, content-type, Authorization"
          }
      },
}