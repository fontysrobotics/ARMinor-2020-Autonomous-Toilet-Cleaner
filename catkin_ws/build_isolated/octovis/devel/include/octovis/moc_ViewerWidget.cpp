/****************************************************************************
** Meta object code from reading C++ file 'ViewerWidget.h'
**
** Created by: The Qt Meta Object Compiler version 67 (Qt 5.9.5)
**
** WARNING! All changes made in this file will be lost!
*****************************************************************************/

#include "../../../../../src/octomap/octovis/include/octovis/ViewerWidget.h"
#include <QtCore/qbytearray.h>
#include <QtCore/qmetatype.h>
#if !defined(Q_MOC_OUTPUT_REVISION)
#error "The header file 'ViewerWidget.h' doesn't include <QObject>."
#elif Q_MOC_OUTPUT_REVISION != 67
#error "This file was generated using the moc from 5.9.5. It"
#error "cannot be used with the include files from this version of Qt."
#error "(The moc has changed too much.)"
#endif

QT_BEGIN_MOC_NAMESPACE
QT_WARNING_PUSH
QT_WARNING_DISABLE_DEPRECATED
struct qt_meta_stringdata_octomap__ViewerWidget_t {
    QByteArrayData data[40];
    char stringdata0[545];
};
#define QT_MOC_LITERAL(idx, ofs, len) \
    Q_STATIC_BYTE_ARRAY_DATA_HEADER_INITIALIZER_WITH_OFFSET(len, \
    qptrdiff(offsetof(qt_meta_stringdata_octomap__ViewerWidget_t, stringdata0) + ofs \
        - idx * sizeof(QByteArrayData)) \
    )
static const qt_meta_stringdata_octomap__ViewerWidget_t qt_meta_stringdata_octomap__ViewerWidget = {
    {
QT_MOC_LITERAL(0, 0, 21), // "octomap::ViewerWidget"
QT_MOC_LITERAL(1, 22, 17), // "cameraPathStopped"
QT_MOC_LITERAL(2, 40, 0), // ""
QT_MOC_LITERAL(3, 41, 2), // "id"
QT_MOC_LITERAL(4, 44, 22), // "cameraPathFrameChanged"
QT_MOC_LITERAL(5, 67, 20), // "current_camera_frame"
QT_MOC_LITERAL(6, 88, 18), // "enablePrintoutMode"
QT_MOC_LITERAL(7, 107, 7), // "enabled"
QT_MOC_LITERAL(8, 115, 21), // "enableHeightColorMode"
QT_MOC_LITERAL(9, 137, 22), // "enableSemanticColoring"
QT_MOC_LITERAL(10, 160, 18), // "enableSelectionBox"
QT_MOC_LITERAL(11, 179, 14), // "setCamPosition"
QT_MOC_LITERAL(12, 194, 1), // "x"
QT_MOC_LITERAL(13, 196, 1), // "y"
QT_MOC_LITERAL(14, 198, 1), // "z"
QT_MOC_LITERAL(15, 200, 5), // "lookX"
QT_MOC_LITERAL(16, 206, 5), // "lookY"
QT_MOC_LITERAL(17, 212, 5), // "lookZ"
QT_MOC_LITERAL(18, 218, 10), // "setCamPose"
QT_MOC_LITERAL(19, 229, 16), // "octomath::Pose6D"
QT_MOC_LITERAL(20, 246, 4), // "pose"
QT_MOC_LITERAL(21, 251, 19), // "setSceneBoundingBox"
QT_MOC_LITERAL(22, 271, 14), // "qglviewer::Vec"
QT_MOC_LITERAL(23, 286, 3), // "min"
QT_MOC_LITERAL(24, 290, 3), // "max"
QT_MOC_LITERAL(25, 294, 16), // "deleteCameraPath"
QT_MOC_LITERAL(26, 311, 18), // "appendToCameraPath"
QT_MOC_LITERAL(27, 330, 25), // "appendCurrentToCameraPath"
QT_MOC_LITERAL(28, 356, 22), // "addCurrentToCameraPath"
QT_MOC_LITERAL(29, 379, 5), // "frame"
QT_MOC_LITERAL(30, 385, 20), // "removeFromCameraPath"
QT_MOC_LITERAL(31, 406, 16), // "updateCameraPath"
QT_MOC_LITERAL(32, 423, 14), // "jumpToCamFrame"
QT_MOC_LITERAL(33, 438, 14), // "playCameraPath"
QT_MOC_LITERAL(34, 453, 11), // "start_frame"
QT_MOC_LITERAL(35, 465, 14), // "stopCameraPath"
QT_MOC_LITERAL(36, 480, 12), // "selectionBox"
QT_MOC_LITERAL(37, 493, 9), // "resetView"
QT_MOC_LITERAL(38, 503, 18), // "cameraPathFinished"
QT_MOC_LITERAL(39, 522, 22) // "cameraPathInterpolated"

    },
    "octomap::ViewerWidget\0cameraPathStopped\0"
    "\0id\0cameraPathFrameChanged\0"
    "current_camera_frame\0enablePrintoutMode\0"
    "enabled\0enableHeightColorMode\0"
    "enableSemanticColoring\0enableSelectionBox\0"
    "setCamPosition\0x\0y\0z\0lookX\0lookY\0lookZ\0"
    "setCamPose\0octomath::Pose6D\0pose\0"
    "setSceneBoundingBox\0qglviewer::Vec\0"
    "min\0max\0deleteCameraPath\0appendToCameraPath\0"
    "appendCurrentToCameraPath\0"
    "addCurrentToCameraPath\0frame\0"
    "removeFromCameraPath\0updateCameraPath\0"
    "jumpToCamFrame\0playCameraPath\0start_frame\0"
    "stopCameraPath\0selectionBox\0resetView\0"
    "cameraPathFinished\0cameraPathInterpolated"
};
#undef QT_MOC_LITERAL

static const uint qt_meta_data_octomap__ViewerWidget[] = {

 // content:
       7,       // revision
       0,       // classname
       0,    0, // classinfo
      26,   14, // methods
       0,    0, // properties
       0,    0, // enums/sets
       0,    0, // constructors
       0,       // flags
       2,       // signalCount

 // signals: name, argc, parameters, tag, flags
       1,    1,  144,    2, 0x06 /* Public */,
       4,    2,  147,    2, 0x06 /* Public */,

 // slots: name, argc, parameters, tag, flags
       6,    1,  152,    2, 0x0a /* Public */,
       6,    0,  155,    2, 0x2a /* Public | MethodCloned */,
       8,    1,  156,    2, 0x0a /* Public */,
       8,    0,  159,    2, 0x2a /* Public | MethodCloned */,
       9,    1,  160,    2, 0x0a /* Public */,
       9,    0,  163,    2, 0x2a /* Public | MethodCloned */,
      10,    1,  164,    2, 0x0a /* Public */,
      10,    0,  167,    2, 0x2a /* Public | MethodCloned */,
      11,    6,  168,    2, 0x0a /* Public */,
      18,    1,  181,    2, 0x0a /* Public */,
      21,    2,  184,    2, 0x0a /* Public */,
      25,    1,  189,    2, 0x0a /* Public */,
      26,    2,  192,    2, 0x0a /* Public */,
      27,    1,  197,    2, 0x0a /* Public */,
      28,    2,  200,    2, 0x0a /* Public */,
      30,    2,  205,    2, 0x0a /* Public */,
      31,    2,  210,    2, 0x0a /* Public */,
      32,    2,  215,    2, 0x0a /* Public */,
      33,    2,  220,    2, 0x0a /* Public */,
      35,    1,  225,    2, 0x0a /* Public */,
      36,    0,  228,    2, 0x0a /* Public */,
      37,    0,  229,    2, 0x0a /* Public */,
      38,    0,  230,    2, 0x08 /* Private */,
      39,    0,  231,    2, 0x08 /* Private */,

 // signals: parameters
    QMetaType::Void, QMetaType::Int,    3,
    QMetaType::Void, QMetaType::Int, QMetaType::Int,    3,    5,

 // slots: parameters
    QMetaType::Void, QMetaType::Bool,    7,
    QMetaType::Void,
    QMetaType::Void, QMetaType::Bool,    7,
    QMetaType::Void,
    QMetaType::Void, QMetaType::Bool,    7,
    QMetaType::Void,
    QMetaType::Void, QMetaType::Bool,    7,
    QMetaType::Void,
    QMetaType::Void, QMetaType::Double, QMetaType::Double, QMetaType::Double, QMetaType::Double, QMetaType::Double, QMetaType::Double,   12,   13,   14,   15,   16,   17,
    QMetaType::Void, 0x80000000 | 19,   20,
    QMetaType::Void, 0x80000000 | 22, 0x80000000 | 22,   23,   24,
    QMetaType::Void, QMetaType::Int,    3,
    QMetaType::Void, QMetaType::Int, 0x80000000 | 19,    3,   20,
    QMetaType::Void, QMetaType::Int,    3,
    QMetaType::Void, QMetaType::Int, QMetaType::Int,    3,   29,
    QMetaType::Void, QMetaType::Int, QMetaType::Int,    3,   29,
    QMetaType::Void, QMetaType::Int, QMetaType::Int,    3,   29,
    QMetaType::Void, QMetaType::Int, QMetaType::Int,    3,   29,
    QMetaType::Void, QMetaType::Int, QMetaType::Int,    3,   34,
    QMetaType::Void, QMetaType::Int,    3,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void,

       0        // eod
};

void octomap::ViewerWidget::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    if (_c == QMetaObject::InvokeMetaMethod) {
        ViewerWidget *_t = static_cast<ViewerWidget *>(_o);
        Q_UNUSED(_t)
        switch (_id) {
        case 0: _t->cameraPathStopped((*reinterpret_cast< int(*)>(_a[1]))); break;
        case 1: _t->cameraPathFrameChanged((*reinterpret_cast< int(*)>(_a[1])),(*reinterpret_cast< int(*)>(_a[2]))); break;
        case 2: _t->enablePrintoutMode((*reinterpret_cast< bool(*)>(_a[1]))); break;
        case 3: _t->enablePrintoutMode(); break;
        case 4: _t->enableHeightColorMode((*reinterpret_cast< bool(*)>(_a[1]))); break;
        case 5: _t->enableHeightColorMode(); break;
        case 6: _t->enableSemanticColoring((*reinterpret_cast< bool(*)>(_a[1]))); break;
        case 7: _t->enableSemanticColoring(); break;
        case 8: _t->enableSelectionBox((*reinterpret_cast< bool(*)>(_a[1]))); break;
        case 9: _t->enableSelectionBox(); break;
        case 10: _t->setCamPosition((*reinterpret_cast< double(*)>(_a[1])),(*reinterpret_cast< double(*)>(_a[2])),(*reinterpret_cast< double(*)>(_a[3])),(*reinterpret_cast< double(*)>(_a[4])),(*reinterpret_cast< double(*)>(_a[5])),(*reinterpret_cast< double(*)>(_a[6]))); break;
        case 11: _t->setCamPose((*reinterpret_cast< const octomath::Pose6D(*)>(_a[1]))); break;
        case 12: _t->setSceneBoundingBox((*reinterpret_cast< const qglviewer::Vec(*)>(_a[1])),(*reinterpret_cast< const qglviewer::Vec(*)>(_a[2]))); break;
        case 13: _t->deleteCameraPath((*reinterpret_cast< int(*)>(_a[1]))); break;
        case 14: _t->appendToCameraPath((*reinterpret_cast< int(*)>(_a[1])),(*reinterpret_cast< const octomath::Pose6D(*)>(_a[2]))); break;
        case 15: _t->appendCurrentToCameraPath((*reinterpret_cast< int(*)>(_a[1]))); break;
        case 16: _t->addCurrentToCameraPath((*reinterpret_cast< int(*)>(_a[1])),(*reinterpret_cast< int(*)>(_a[2]))); break;
        case 17: _t->removeFromCameraPath((*reinterpret_cast< int(*)>(_a[1])),(*reinterpret_cast< int(*)>(_a[2]))); break;
        case 18: _t->updateCameraPath((*reinterpret_cast< int(*)>(_a[1])),(*reinterpret_cast< int(*)>(_a[2]))); break;
        case 19: _t->jumpToCamFrame((*reinterpret_cast< int(*)>(_a[1])),(*reinterpret_cast< int(*)>(_a[2]))); break;
        case 20: _t->playCameraPath((*reinterpret_cast< int(*)>(_a[1])),(*reinterpret_cast< int(*)>(_a[2]))); break;
        case 21: _t->stopCameraPath((*reinterpret_cast< int(*)>(_a[1]))); break;
        case 22: _t->selectionBox(); break;
        case 23: _t->resetView(); break;
        case 24: _t->cameraPathFinished(); break;
        case 25: _t->cameraPathInterpolated(); break;
        default: ;
        }
    } else if (_c == QMetaObject::IndexOfMethod) {
        int *result = reinterpret_cast<int *>(_a[0]);
        {
            typedef void (ViewerWidget::*_t)(int );
            if (*reinterpret_cast<_t *>(_a[1]) == static_cast<_t>(&ViewerWidget::cameraPathStopped)) {
                *result = 0;
                return;
            }
        }
        {
            typedef void (ViewerWidget::*_t)(int , int );
            if (*reinterpret_cast<_t *>(_a[1]) == static_cast<_t>(&ViewerWidget::cameraPathFrameChanged)) {
                *result = 1;
                return;
            }
        }
    }
}

const QMetaObject octomap::ViewerWidget::staticMetaObject = {
    { &QGLViewer::staticMetaObject, qt_meta_stringdata_octomap__ViewerWidget.data,
      qt_meta_data_octomap__ViewerWidget,  qt_static_metacall, nullptr, nullptr}
};


const QMetaObject *octomap::ViewerWidget::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *octomap::ViewerWidget::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_meta_stringdata_octomap__ViewerWidget.stringdata0))
        return static_cast<void*>(this);
    return QGLViewer::qt_metacast(_clname);
}

int octomap::ViewerWidget::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QGLViewer::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    if (_c == QMetaObject::InvokeMetaMethod) {
        if (_id < 26)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 26;
    } else if (_c == QMetaObject::RegisterMethodArgumentMetaType) {
        if (_id < 26)
            *reinterpret_cast<int*>(_a[0]) = -1;
        _id -= 26;
    }
    return _id;
}

// SIGNAL 0
void octomap::ViewerWidget::cameraPathStopped(int _t1)
{
    void *_a[] = { nullptr, const_cast<void*>(reinterpret_cast<const void*>(&_t1)) };
    QMetaObject::activate(this, &staticMetaObject, 0, _a);
}

// SIGNAL 1
void octomap::ViewerWidget::cameraPathFrameChanged(int _t1, int _t2)
{
    void *_a[] = { nullptr, const_cast<void*>(reinterpret_cast<const void*>(&_t1)), const_cast<void*>(reinterpret_cast<const void*>(&_t2)) };
    QMetaObject::activate(this, &staticMetaObject, 1, _a);
}
QT_WARNING_POP
QT_END_MOC_NAMESPACE
