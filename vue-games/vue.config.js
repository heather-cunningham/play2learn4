module.exports = {
  publicPath: 'http://localhost:8080', // The base URL where your app will be deployed 
  outputDir: '../static/dist', // The path for where files will be output when the app is built
  
  /* Removed this indexPath for now, so Vue doesn't overwrite this template every time I
  run `npm run serve` from the Vue games sub-dir root */
  indexPath: '../../templates/_base_vue.html', // The path for the generated index file

  configureWebpack: {
    devServer: {
      devMiddleware: {
        writeToDisk: true
      }
    }
  }
};

/* Not using this default config: */
// const { defineConfig } = require('@vue/cli-service')
// module.exports = defineConfig({
//   transpileDependencies: true
// })
