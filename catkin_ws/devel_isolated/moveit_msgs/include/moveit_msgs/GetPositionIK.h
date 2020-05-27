// Generated by gencpp from file moveit_msgs/GetPositionIK.msg
// DO NOT EDIT!


#ifndef MOVEIT_MSGS_MESSAGE_GETPOSITIONIK_H
#define MOVEIT_MSGS_MESSAGE_GETPOSITIONIK_H

#include <ros/service_traits.h>


#include <moveit_msgs/GetPositionIKRequest.h>
#include <moveit_msgs/GetPositionIKResponse.h>


namespace moveit_msgs
{

struct GetPositionIK
{

typedef GetPositionIKRequest Request;
typedef GetPositionIKResponse Response;
Request request;
Response response;

typedef Request RequestType;
typedef Response ResponseType;

}; // struct GetPositionIK
} // namespace moveit_msgs


namespace ros
{
namespace service_traits
{


template<>
struct MD5Sum< ::moveit_msgs::GetPositionIK > {
  static const char* value()
  {
    return "7314d1f4b17db70d01b1a71c8c516c39";
  }

  static const char* value(const ::moveit_msgs::GetPositionIK&) { return value(); }
};

template<>
struct DataType< ::moveit_msgs::GetPositionIK > {
  static const char* value()
  {
    return "moveit_msgs/GetPositionIK";
  }

  static const char* value(const ::moveit_msgs::GetPositionIK&) { return value(); }
};


// service_traits::MD5Sum< ::moveit_msgs::GetPositionIKRequest> should match
// service_traits::MD5Sum< ::moveit_msgs::GetPositionIK >
template<>
struct MD5Sum< ::moveit_msgs::GetPositionIKRequest>
{
  static const char* value()
  {
    return MD5Sum< ::moveit_msgs::GetPositionIK >::value();
  }
  static const char* value(const ::moveit_msgs::GetPositionIKRequest&)
  {
    return value();
  }
};

// service_traits::DataType< ::moveit_msgs::GetPositionIKRequest> should match
// service_traits::DataType< ::moveit_msgs::GetPositionIK >
template<>
struct DataType< ::moveit_msgs::GetPositionIKRequest>
{
  static const char* value()
  {
    return DataType< ::moveit_msgs::GetPositionIK >::value();
  }
  static const char* value(const ::moveit_msgs::GetPositionIKRequest&)
  {
    return value();
  }
};

// service_traits::MD5Sum< ::moveit_msgs::GetPositionIKResponse> should match
// service_traits::MD5Sum< ::moveit_msgs::GetPositionIK >
template<>
struct MD5Sum< ::moveit_msgs::GetPositionIKResponse>
{
  static const char* value()
  {
    return MD5Sum< ::moveit_msgs::GetPositionIK >::value();
  }
  static const char* value(const ::moveit_msgs::GetPositionIKResponse&)
  {
    return value();
  }
};

// service_traits::DataType< ::moveit_msgs::GetPositionIKResponse> should match
// service_traits::DataType< ::moveit_msgs::GetPositionIK >
template<>
struct DataType< ::moveit_msgs::GetPositionIKResponse>
{
  static const char* value()
  {
    return DataType< ::moveit_msgs::GetPositionIK >::value();
  }
  static const char* value(const ::moveit_msgs::GetPositionIKResponse&)
  {
    return value();
  }
};

} // namespace service_traits
} // namespace ros

#endif // MOVEIT_MSGS_MESSAGE_GETPOSITIONIK_H
