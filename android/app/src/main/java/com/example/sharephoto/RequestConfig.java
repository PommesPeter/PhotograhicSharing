package com.example.sharephoto;

public class RequestConfig {
    public static String URL = "http://pan.kexie.space:9192/";                      //url

    //    用户
    public static String LOGIN = URL + "users/login";                               //登录
    public static String REGISTER = URL + "users/register";                         //注册
    public static String MODIFY_AVATAR = URL + "user/modify_avatar";                //修改头像
    public static String SHOW_USER = URL + "user/show_user";                        //用户信息
    public static String MODIFY_INFO = URL + "user/modify_user_info";               //修改用户信息

    //说说
    public static String RECOMMEND = URL + "shuoshuo/recommended";                  //推荐列表
    public static String CONCERN = URL + "shuoshuo/concern";                        //关注列表
    public static String DETAIL = URL + "shuoshuo/detail";                          //说说内容
    public static String THUMBSUP = URL + "shuoshuo/thumpsup";                      //点赞
    public static String FOLLOW = URL + "shuoshuo/follow";                          //关注作者
    public static String FAVOR = URL + "shuoshuo/favor";                            //收藏
    public static String PUBLISH = URL + "shuoshuo/publish";                        //发布说说

    //    图像
    public static String UPLOAD_IMAGES = URL + "images/upload_imgs";                //上传图像
    public static String UPLOAD_AVATAR = URL + "images/upload_avatar";              //上传头像

    //    评论
    public static String COMMENT_THUMBSUP = URL + "comment/thumbsup";               //评论点赞
    public static String PUBLISH_COMMENT = URL + "comment/publish_comment";         //发表评论
    public static String GET_COMMENT = URL + "comment/get_comment";                 //获取评论
}
