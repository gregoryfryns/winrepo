const BundleTracker = require('webpack-bundle-tracker');
const fileLoader = require('file-loader');

module.exports = {
  configureWebpack: {
    module: {
      rules: [
        {
          test: /\.(pdf)(\?.*)?$/,
          use: [
            {
              loader: 'file-loader',
              options: {
                name: 'assets/[name].[hash:8].[ext]',
                esModule: false
              }
            }
          ]
        }
      ]
    }
  },

  // on Windows you might want to set publicPath: "http://127.0.0.1:8080/"
  publicPath: 'http://0.0.0.0:8080/',
  outputDir: './dist/',

  chainWebpack: config => {
    config
      .plugin('BundleTracker')
      .use(BundleTracker, [{ filename: './webpack-stats.json' }]);

    config.output.filename('bundle.js');

    config.optimization.splitChunks(false);

    config.resolve.alias.set('__STATIC__', 'static');

    // config.module
    //   .rule('pdf')
    //   .test(/\.pdf$/)
    //   .use('file-loader')
    //     .loader('file-loader')
    //     // .tap(options => {
    //     //   // modify the options..
    //     //   // options.esModule = false;
    //     //   return options
    //     // })
    //     .end()

    config.devServer
      // the first 3 lines of the following code have been added to the configuration
      .public('http://127.0.0.1:8080')
      .host('127.0.0.1')
      .port(8080)
      .hotOnly(true)
      .watchOptions({ poll: 1000 })
      .https(false)
      .disableHostCheck(true)
      .headers({ 'Access-Control-Allow-Origin': ['*'] });
  },

  // uncomment before executing 'npm run build'
  css: {
    extract: {
      filename: 'bundle.css',
      chunkFilename: 'bundle.css'
    }
  }
};
