// Import dependencies
const path = require('path');

const config = {
  entry: './character_creator/frontend/src/index.js',
    output: {
        path: path.resolve(__dirname,'character_creator/frontend/static/frontend'),
        filename: 'main.js',
    },
  module: {
    rules: [
      {
        test: /\.js$/,
        exclude: /node_modules/,
        use: {
          loader: "babel-loader"
        }
      },
      {
        test: /\.css$/,
        use: [
          {loader: 'style-loader'},
          {
            loader: 'css-loader',
            options: {
              modules: true
            }
          },
          {loader: 'sass-loader'}
        ]
      },
      {
        test: /\.(png|jp(e*)g|svg|gif|)$/,
        use: [{
          loader: 'url-loader',
          options: {
            limit: 8000, // Convert images < 8kb to base64 strings
            name: 'images/[path][name]-[hash:8].[ext]'
          }
        }]
      }
    ]
  }
};

module.exports = config;
