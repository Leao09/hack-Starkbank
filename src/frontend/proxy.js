const { createProxyMiddleware } = require("http-proxy-middleware");

module.exports = function (app) {
  app.use(
    "/metabase-proxy",
    createProxyMiddleware({
      target: "https://localhost:3000",
      changeOrigin: true,
      pathRewrite: {
        "^/metabase-proxy": "",
      },
      onProxyReq: (proxyReq) => {
        proxyReq.setHeader(
          "Authorization",
          "Bearer mb_Wznquf7gutKaF5lAki5A64vDXxCmdANH4hrxM4mslyc="
        );
      },
    })
  );
};
