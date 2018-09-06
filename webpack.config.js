// Import dependencies
const path = require('path');
const ExtractTextPlugin  = require('extract-text-webpack-plugin');

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
        use: ExtractTextPlugin.extract(
          {
            fallback: 'style-loader',
            use: ['css-loader']
          })
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
  },
  plugins: [
    new ExtractTextPlugin({filename: 'style.css'})
  ]
};

module.exports = config;
