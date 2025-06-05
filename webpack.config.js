const path = require('path');

module.exports ={
    mode: 'development',
    entry:{
      './index':'./assets/scripts/index.js',
      './homePage':'./assets/scripts/homePage.js',
      './productDetails':'./assets/scripts/productDetails.js',
      './products_list':'./assets/scripts/products_list.js',
      './list_of_buy':'./assets/scripts/list_of_buy.js',
      './list_of_buy_css':'./assets/styles/list_of_buy.css',
      './post_order':'./assets/scripts/post_order.js',
      './add_post_address':'./assets/scripts/add_post_address.js',
      './paymentMethod':'./assets/scripts/paymentMethod.js',
      
      './post_order_css':'./assets/styles/post_order.css',
      './add_post_address_css':'./assets/styles/add_post_address.css',
      './add_userAdressDetail_css':'./assets/styles/add_userAdressDetail.css',
      './paymentMethod_css':'./assets/styles/paymentMethod.css',
    },
    output: {
        // publicPath:'http://127.0.0.1:8080/',
        // path: path.resolve(__dirname, 'homePage', 'static'),
        path: path.resolve(__dirname, 'assets', 'js'),
        // filename: 'bundle.js',
        // path: path.resolve(__dirname, 'dist'),
        filename: '[name].js'
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