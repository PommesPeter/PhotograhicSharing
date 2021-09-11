package com.example.sharephoto;

import android.content.Context;
import android.content.SharedPreferences;

public class RequestConfig {
    public static String URL = "http://172.16.75.73:9192/";                      //url

    //    用户
    public static String LOGIN = URL + "users/login";                               //登录
    public static String REGISTER = URL + "users/register";                         //注册
    public static String MODIFY_AVATAR = URL + "users/modify_avatar";                //修改头像
    public static String SHOW_USER = URL + "users/show_user_info";                   //用户信息
    public static String MODIFY_INFO = URL + "users/modify_user_info";               //修改用户信息

    //说说
    public static String RECOMMEND = URL + "shuoshuo/recommended";                  //推荐列表
    public static String CONCERN = URL + "shuoshuo/concern";                        //关注列表
    public static String DETAIL = URL + "shuoshuo/detail";                          //说说内容
    public static String THUMBSUP = URL + "shuoshuo/thumbsup";                      //点赞
    public static String FOLLOW = URL + "shuoshuo/follow";                          //关注作者
    public static String FAVOR = URL + "shuoshuo/favor";                            //收藏
    public static String PUBLISH = URL + "shuoshuo/publish";                        //发布说说
    public static String CATEGORY = URL + "shuoshuo/category";                      //分类

    //    图像
    public static String UPLOAD_IMAGES = URL + "images/upload_imgs";                //上传图像
    public static String UPLOAD_AVATAR = URL + "images/upload_avatar";              //上传头像

    //    评论
    public static String COMMENT_THUMBSUP = URL + "comments/thumbsup_comments";               //评论点赞
    public static String PUBLISH_COMMENT = URL + "comments/publish_comments";         //发表评论
    public static String GET_COMMENT = URL + "comments/get_comments";                 //获取评论

}
