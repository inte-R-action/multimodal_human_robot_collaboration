#ifndef SAM_CUSTOM_MESSAGES__VISIBILITY_CONTROL_H_
#define SAM_CUSTOM_MESSAGES__VISIBILITY_CONTROL_H_
#if defined _WIN32 || defined __CYGWIN__
  #ifdef __GNUC__
    #define SAM_CUSTOM_MESSAGES_EXPORT __attribute__ ((dllexport))
    #define SAM_CUSTOM_MESSAGES_IMPORT __attribute__ ((dllimport))
  #else
    #define SAM_CUSTOM_MESSAGES_EXPORT __declspec(dllexport)
    #define SAM_CUSTOM_MESSAGES_IMPORT __declspec(dllimport)
  #endif
  #ifdef SAM_CUSTOM_MESSAGES_BUILDING_LIBRARY
    #define SAM_CUSTOM_MESSAGES_PUBLIC SAM_CUSTOM_MESSAGES_EXPORT
  #else
    #define SAM_CUSTOM_MESSAGES_PUBLIC SAM_CUSTOM_MESSAGES_IMPORT
  #endif
  #define SAM_CUSTOM_MESSAGES_PUBLIC_TYPE SAM_CUSTOM_MESSAGES_PUBLIC
  #define SAM_CUSTOM_MESSAGES_LOCAL
#else
  #define SAM_CUSTOM_MESSAGES_EXPORT __attribute__ ((visibility("default")))
  #define SAM_CUSTOM_MESSAGES_IMPORT
  #if __GNUC__ >= 4
    #define SAM_CUSTOM_MESSAGES_PUBLIC __attribute__ ((visibility("default")))
    #define SAM_CUSTOM_MESSAGES_LOCAL  __attribute__ ((visibility("hidden")))
  #else
    #define SAM_CUSTOM_MESSAGES_PUBLIC
    #define SAM_CUSTOM_MESSAGES_LOCAL
  #endif
  #define SAM_CUSTOM_MESSAGES_PUBLIC_TYPE
#endif
#endif  // SAM_CUSTOM_MESSAGES__VISIBILITY_CONTROL_H_
// Generated 15-Nov-2020 15:33:04
// Copyright 2019-2020 The MathWorks, Inc.
