// Copyright 2019-2020 The MathWorks, Inc.
// Common copy functions for sam_custom_messages/Object
#include "boost/date_time.hpp"
#include "boost/shared_array.hpp"
#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable : 4244)
#pragma warning(disable : 4265)
#pragma warning(disable : 4458)
#pragma warning(disable : 4100)
#pragma warning(disable : 4127)
#pragma warning(disable : 4267)
#else
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wpedantic"
#pragma GCC diagnostic ignored "-Wunused-local-typedefs"
#pragma GCC diagnostic ignored "-Wredundant-decls"
#pragma GCC diagnostic ignored "-Wnon-virtual-dtor"
#pragma GCC diagnostic ignored "-Wdelete-non-virtual-dtor"
#pragma GCC diagnostic ignored "-Wunused-parameter"
#pragma GCC diagnostic ignored "-Wunused-variable"
#pragma GCC diagnostic ignored "-Wshadow"
#endif //_MSC_VER
#include "ros/ros.h"
#include "sam_custom_messages/Object.h"
#include "visibility_control.h"
#ifndef FOUNDATION_MATLABDATA_API
#include "MDArray.hpp"
#include "StructArray.hpp"
#include "TypedArrayRef.hpp"
#include "Struct.hpp"
#include "ArrayFactory.hpp"
#include "StructRef.hpp"
#include "Reference.hpp"
#endif
#ifndef FOUNDATION_MATLABDATA_API
typedef matlab::data::Array MDArray_T;
typedef matlab::data::ArrayFactory MDFactory_T;
#else
typedef foundation::matlabdata::Array MDArray_T;
typedef foundation::matlabdata::standalone::ClientArrayFactory MDFactory_T;
#endif
namespace sam_custom_messages {
namespace matlabhelper {
namespace Object {
  //----------------------------------------------------------------------------
  SAM_CUSTOM_MESSAGES_EXPORT void copy_from_arr(boost::shared_ptr<sam_custom_messages::Object>& msg, const matlab::data::StructArray arr) {
    try {
        //id
        const matlab::data::TypedArray<int8_t> id_arr = arr[0]["id"];
        msg->id = id_arr[0];
    } catch (matlab::data::InvalidFieldNameException&) {
        throw std::invalid_argument("Field 'id' is missing.");
    } catch (matlab::data::TypeMismatchException&) {
        throw std::invalid_argument("Field 'id' is wrong type; expected a int8.");
    }
    try {
        //type
        const matlab::data::TypedArray<int8_t> type_arr = arr[0]["type"];
        msg->type = type_arr[0];
    } catch (matlab::data::InvalidFieldNameException&) {
        throw std::invalid_argument("Field 'type' is missing.");
    } catch (matlab::data::TypeMismatchException&) {
        throw std::invalid_argument("Field 'type' is wrong type; expected a int8.");
    }
    try {
        //info
        const matlab::data::CellArray info_cellarr = arr[0]["info"];
        size_t nelem = info_cellarr.getNumberOfElements();
        for (size_t idx=0; idx < nelem; ++idx){
        	const matlab::data::CharArray info_arr = info_cellarr[idx];
        	msg->info.push_back(info_arr.toAscii());
        }
    } catch (matlab::data::InvalidFieldNameException&) {
        throw std::invalid_argument("Field 'info' is missing.");
    } catch (matlab::data::TypeMismatchException&) {
        throw std::invalid_argument("Field 'info' is wrong type; expected a string.");
    }
  }
  //----------------------------------------------------------------------------
  SAM_CUSTOM_MESSAGES_EXPORT MDArray_T get_arr(MDFactory_T& factory, const boost::shared_ptr<const sam_custom_messages::Object>& msg) {
    auto outArray = factory.createStructArray({1,1},{"id","type","info"});
    // id
    outArray[0]["id"] = factory.createScalar(msg->id);
    // type
    outArray[0]["type"] = factory.createScalar(msg->type);
    // info
    auto infooutCell = factory.createCellArray({1,msg->info.size()});
    for(size_t idxin = 0; idxin < msg->info.size(); ++ idxin){
    	infooutCell[idxin] = factory.createCharArray(msg->info[idxin]);
    }
    outArray[0]["info"] = infooutCell;
    return std::move(outArray);
  }
} //namespace Object
} //namespace matlabhelper
} //namespace sam_custom_messages
#ifdef _MSC_VER
#pragma warning(pop)
#else
#pragma GCC diagnostic pop
#endif //_MSC_VER
//gen-1