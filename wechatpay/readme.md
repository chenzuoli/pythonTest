# 常用的5种支付产品
1. JSAPI支付
适用场景：适用于已接入微信公众平台的网页应用，用户在微信内置浏览器中打开商户网页时使用。
2. APP支付
适用场景：适用于移动端应用（如Android、iOS App），用户通过App内调用微信支付SDK完成支付。
3. H5支付
适用场景：适用于在非微信浏览器中打开的移动网页支付场景，例如通过短信链接或扫码在手机浏览器中打开的支付页面。
4. Native支付
适用场景：适用于线下实体场景，例如商户系统生成二维码供用户扫码支付（如超市、便利店等）。
5. 小程序支付
适用场景：适用于微信小程序内的支付流程，用户在小程序内选购商品或服务后完成支付。

接入文档：https://pay.weixin.qq.com/doc/v3/partner/4012069852

# 两种验签方式
1. 验签方式一：平台证书方式
2. 验签方式二：微信支付公钥方式

因为每张平台证书有效期为5年，如果未及时更换会影响业务，建议使用微信支付公钥模式对接，可以按需更新公钥。

如果你是第一次对接微信支付，此前从未使用过平台证书，请参考微信支付公钥指引 完成对接。

不同：
https://pay.weixin.qq.com/doc/v3/partner/4012925323


# 申请
https://pay.weixin.qq.com/index.php/core/cert/api_cert#/

