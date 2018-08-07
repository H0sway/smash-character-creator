const ExtractTextWebpackPlugin = require('extract-text-webpack-plugin');

const config = {
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
        use: ExtractTextWebpackPlugin.extract({
          use: 'css-loader'
        }),
        test: /\.css$/
      },
      {
        test: /\.(png|jp(e*)g|svg)$/,
        use: [{
          loader: 'url-loader',
          options: {
            limit: 8000, // Convert images < 8kb to base64 strings
            name: 'images/[hash]-[name].[ext]'
          }
        }]
      }
    ]
  }
  plugins: [
    new ExtractTextWebpackPlugin('style.css')
  ]
};

module.exports = config;
