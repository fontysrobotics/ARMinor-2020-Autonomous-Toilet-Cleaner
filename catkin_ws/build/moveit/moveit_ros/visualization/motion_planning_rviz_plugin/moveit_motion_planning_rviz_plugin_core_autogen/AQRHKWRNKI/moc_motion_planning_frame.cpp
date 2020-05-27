/****************************************************************************
** Meta object code from reading C++ file 'motion_planning_frame.h'
**
** Created by: The Qt Meta Object Compiler version 67 (Qt 5.9.5)
**
** WARNING! All changes made in this file will be lost!
*****************************************************************************/

#include "../../../../../../../src/moveit/moveit_ros/visualization/motion_planning_rviz_plugin/include/moveit/motion_planning_rviz_plugin/motion_planning_frame.h"
#include <QtCore/qbytearray.h>
#include <QtCore/qmetatype.h>
#if !defined(Q_MOC_OUTPUT_REVISION)
#error "The header file 'motion_planning_frame.h' doesn't include <QObject>."
#elif Q_MOC_OUTPUT_REVISION != 67
#error "This file was generated using the moc from 5.9.5. It"
#error "cannot be used with the include files from this version of Qt."
#error "(The moc has changed too much.)"
#endif

QT_BEGIN_MOC_NAMESPACE
QT_WARNING_PUSH
QT_WARNING_DISABLE_DEPRECATED
struct qt_meta_stringdata_moveit_rviz_plugin__MotionPlanningFrame_t {
    QByteArrayData data[74];
    char stringdata0[1599];
};
#define QT_MOC_LITERAL(idx, ofs, len) \
    Q_STATIC_BYTE_ARRAY_DATA_HEADER_INITIALIZER_WITH_OFFSET(len, \
    qptrdiff(offsetof(qt_meta_stringdata_moveit_rviz_plugin__MotionPlanningFrame_t, stringdata0) + ofs \
        - idx * sizeof(QByteArrayData)) \
    )
static const qt_meta_stringdata_moveit_rviz_plugin__MotionPlanningFrame_t qt_meta_stringdata_moveit_rviz_plugin__MotionPlanningFrame = {
    {
QT_MOC_LITERAL(0, 0, 39), // "moveit_rviz_plugin::MotionPla..."
QT_MOC_LITERAL(1, 40, 16), // "planningFinished"
QT_MOC_LITERAL(2, 57, 0), // ""
QT_MOC_LITERAL(3, 58, 13), // "configChanged"
QT_MOC_LITERAL(4, 72, 28), // "databaseConnectButtonClicked"
QT_MOC_LITERAL(5, 101, 25), // "publishSceneButtonClicked"
QT_MOC_LITERAL(6, 127, 29), // "planningAlgorithmIndexChanged"
QT_MOC_LITERAL(7, 157, 5), // "index"
QT_MOC_LITERAL(8, 163, 20), // "resetDbButtonClicked"
QT_MOC_LITERAL(9, 184, 20), // "approximateIKChanged"
QT_MOC_LITERAL(10, 205, 5), // "state"
QT_MOC_LITERAL(11, 211, 20), // "computeCartesianPlan"
QT_MOC_LITERAL(12, 232, 21), // "computeJointSpacePlan"
QT_MOC_LITERAL(13, 254, 17), // "planButtonClicked"
QT_MOC_LITERAL(14, 272, 20), // "executeButtonClicked"
QT_MOC_LITERAL(15, 293, 27), // "planAndExecuteButtonClicked"
QT_MOC_LITERAL(16, 321, 17), // "stopButtonClicked"
QT_MOC_LITERAL(17, 339, 22), // "allowReplanningToggled"
QT_MOC_LITERAL(18, 362, 7), // "checked"
QT_MOC_LITERAL(19, 370, 19), // "allowLookingToggled"
QT_MOC_LITERAL(20, 390, 33), // "allowExternalProgramCommunica..."
QT_MOC_LITERAL(21, 424, 6), // "enable"
QT_MOC_LITERAL(22, 431, 27), // "pathConstraintsIndexChanged"
QT_MOC_LITERAL(23, 459, 23), // "onNewPlanningSceneState"
QT_MOC_LITERAL(24, 483, 21), // "startStateTextChanged"
QT_MOC_LITERAL(25, 505, 11), // "start_state"
QT_MOC_LITERAL(26, 517, 20), // "goalStateTextChanged"
QT_MOC_LITERAL(27, 538, 10), // "goal_state"
QT_MOC_LITERAL(28, 549, 24), // "planningGroupTextChanged"
QT_MOC_LITERAL(29, 574, 14), // "planning_group"
QT_MOC_LITERAL(30, 589, 21), // "onClearOctomapClicked"
QT_MOC_LITERAL(31, 611, 23), // "importFileButtonClicked"
QT_MOC_LITERAL(32, 635, 22), // "importUrlButtonClicked"
QT_MOC_LITERAL(33, 658, 23), // "clearSceneButtonClicked"
QT_MOC_LITERAL(34, 682, 17), // "sceneScaleChanged"
QT_MOC_LITERAL(35, 700, 5), // "value"
QT_MOC_LITERAL(36, 706, 21), // "sceneScaleStartChange"
QT_MOC_LITERAL(37, 728, 19), // "sceneScaleEndChange"
QT_MOC_LITERAL(38, 748, 25), // "removeObjectButtonClicked"
QT_MOC_LITERAL(39, 774, 30), // "selectedCollisionObjectChanged"
QT_MOC_LITERAL(40, 805, 22), // "objectPoseValueChanged"
QT_MOC_LITERAL(41, 828, 22), // "collisionObjectChanged"
QT_MOC_LITERAL(42, 851, 16), // "QListWidgetItem*"
QT_MOC_LITERAL(43, 868, 4), // "item"
QT_MOC_LITERAL(44, 873, 17), // "imProcessFeedback"
QT_MOC_LITERAL(45, 891, 46), // "visualization_msgs::Interacti..."
QT_MOC_LITERAL(46, 938, 8), // "feedback"
QT_MOC_LITERAL(47, 947, 27), // "copySelectedCollisionObject"
QT_MOC_LITERAL(48, 975, 25), // "exportAsTextButtonClicked"
QT_MOC_LITERAL(49, 1001, 27), // "importFromTextButtonClicked"
QT_MOC_LITERAL(50, 1029, 22), // "saveSceneButtonClicked"
QT_MOC_LITERAL(51, 1052, 24), // "planningSceneItemClicked"
QT_MOC_LITERAL(52, 1077, 22), // "saveQueryButtonClicked"
QT_MOC_LITERAL(53, 1100, 24), // "deleteSceneButtonClicked"
QT_MOC_LITERAL(54, 1125, 24), // "deleteQueryButtonClicked"
QT_MOC_LITERAL(55, 1150, 22), // "loadSceneButtonClicked"
QT_MOC_LITERAL(56, 1173, 22), // "loadQueryButtonClicked"
QT_MOC_LITERAL(57, 1196, 24), // "warehouseItemNameChanged"
QT_MOC_LITERAL(58, 1221, 16), // "QTreeWidgetItem*"
QT_MOC_LITERAL(59, 1238, 6), // "column"
QT_MOC_LITERAL(60, 1245, 22), // "loadStateButtonClicked"
QT_MOC_LITERAL(61, 1268, 27), // "saveStartStateButtonClicked"
QT_MOC_LITERAL(62, 1296, 26), // "saveGoalStateButtonClicked"
QT_MOC_LITERAL(63, 1323, 24), // "removeStateButtonClicked"
QT_MOC_LITERAL(64, 1348, 24), // "clearStatesButtonClicked"
QT_MOC_LITERAL(65, 1373, 28), // "setAsStartStateButtonClicked"
QT_MOC_LITERAL(66, 1402, 27), // "setAsGoalStateButtonClicked"
QT_MOC_LITERAL(67, 1430, 26), // "detectObjectsButtonClicked"
QT_MOC_LITERAL(68, 1457, 23), // "pickObjectButtonClicked"
QT_MOC_LITERAL(69, 1481, 24), // "placeObjectButtonClicked"
QT_MOC_LITERAL(70, 1506, 29), // "selectedDetectedObjectChanged"
QT_MOC_LITERAL(71, 1536, 21), // "detectedObjectChanged"
QT_MOC_LITERAL(72, 1558, 29), // "selectedSupportSurfaceChanged"
QT_MOC_LITERAL(73, 1588, 10) // "tabChanged"

    },
    "moveit_rviz_plugin::MotionPlanningFrame\0"
    "planningFinished\0\0configChanged\0"
    "databaseConnectButtonClicked\0"
    "publishSceneButtonClicked\0"
    "planningAlgorithmIndexChanged\0index\0"
    "resetDbButtonClicked\0approximateIKChanged\0"
    "state\0computeCartesianPlan\0"
    "computeJointSpacePlan\0planButtonClicked\0"
    "executeButtonClicked\0planAndExecuteButtonClicked\0"
    "stopButtonClicked\0allowReplanningToggled\0"
    "checked\0allowLookingToggled\0"
    "allowExternalProgramCommunication\0"
    "enable\0pathConstraintsIndexChanged\0"
    "onNewPlanningSceneState\0startStateTextChanged\0"
    "start_state\0goalStateTextChanged\0"
    "goal_state\0planningGroupTextChanged\0"
    "planning_group\0onClearOctomapClicked\0"
    "importFileButtonClicked\0importUrlButtonClicked\0"
    "clearSceneButtonClicked\0sceneScaleChanged\0"
    "value\0sceneScaleStartChange\0"
    "sceneScaleEndChange\0removeObjectButtonClicked\0"
    "selectedCollisionObjectChanged\0"
    "objectPoseValueChanged\0collisionObjectChanged\0"
    "QListWidgetItem*\0item\0imProcessFeedback\0"
    "visualization_msgs::InteractiveMarkerFeedback&\0"
    "feedback\0copySelectedCollisionObject\0"
    "exportAsTextButtonClicked\0"
    "importFromTextButtonClicked\0"
    "saveSceneButtonClicked\0planningSceneItemClicked\0"
    "saveQueryButtonClicked\0deleteSceneButtonClicked\0"
    "deleteQueryButtonClicked\0"
    "loadSceneButtonClicked\0loadQueryButtonClicked\0"
    "warehouseItemNameChanged\0QTreeWidgetItem*\0"
    "column\0loadStateButtonClicked\0"
    "saveStartStateButtonClicked\0"
    "saveGoalStateButtonClicked\0"
    "removeStateButtonClicked\0"
    "clearStatesButtonClicked\0"
    "setAsStartStateButtonClicked\0"
    "setAsGoalStateButtonClicked\0"
    "detectObjectsButtonClicked\0"
    "pickObjectButtonClicked\0"
    "placeObjectButtonClicked\0"
    "selectedDetectedObjectChanged\0"
    "detectedObjectChanged\0"
    "selectedSupportSurfaceChanged\0tabChanged"
};
#undef QT_MOC_LITERAL

static const uint qt_meta_data_moveit_rviz_plugin__MotionPlanningFrame[] = {

 // content:
       7,       // revision
       0,       // classname
       0,    0, // classinfo
      58,   14, // methods
       0,    0, // properties
       0,    0, // enums/sets
       0,    0, // constructors
       0,       // flags
       2,       // signalCount

 // signals: name, argc, parameters, tag, flags
       1,    0,  304,    2, 0x06 /* Public */,
       3,    0,  305,    2, 0x06 /* Public */,

 // slots: name, argc, parameters, tag, flags
       4,    0,  306,    2, 0x08 /* Private */,
       5,    0,  307,    2, 0x08 /* Private */,
       6,    1,  308,    2, 0x08 /* Private */,
       8,    0,  311,    2, 0x08 /* Private */,
       9,    1,  312,    2, 0x08 /* Private */,
      11,    0,  315,    2, 0x08 /* Private */,
      12,    0,  316,    2, 0x08 /* Private */,
      13,    0,  317,    2, 0x08 /* Private */,
      14,    0,  318,    2, 0x08 /* Private */,
      15,    0,  319,    2, 0x08 /* Private */,
      16,    0,  320,    2, 0x08 /* Private */,
      17,    1,  321,    2, 0x08 /* Private */,
      19,    1,  324,    2, 0x08 /* Private */,
      20,    1,  327,    2, 0x08 /* Private */,
      22,    1,  330,    2, 0x08 /* Private */,
      23,    0,  333,    2, 0x08 /* Private */,
      24,    1,  334,    2, 0x08 /* Private */,
      26,    1,  337,    2, 0x08 /* Private */,
      28,    1,  340,    2, 0x08 /* Private */,
      30,    0,  343,    2, 0x08 /* Private */,
      31,    0,  344,    2, 0x08 /* Private */,
      32,    0,  345,    2, 0x08 /* Private */,
      33,    0,  346,    2, 0x08 /* Private */,
      34,    1,  347,    2, 0x08 /* Private */,
      36,    0,  350,    2, 0x08 /* Private */,
      37,    0,  351,    2, 0x08 /* Private */,
      38,    0,  352,    2, 0x08 /* Private */,
      39,    0,  353,    2, 0x08 /* Private */,
      40,    1,  354,    2, 0x08 /* Private */,
      41,    1,  357,    2, 0x08 /* Private */,
      44,    1,  360,    2, 0x08 /* Private */,
      47,    0,  363,    2, 0x08 /* Private */,
      48,    0,  364,    2, 0x08 /* Private */,
      49,    0,  365,    2, 0x08 /* Private */,
      50,    0,  366,    2, 0x08 /* Private */,
      51,    0,  367,    2, 0x08 /* Private */,
      52,    0,  368,    2, 0x08 /* Private */,
      53,    0,  369,    2, 0x08 /* Private */,
      54,    0,  370,    2, 0x08 /* Private */,
      55,    0,  371,    2, 0x08 /* Private */,
      56,    0,  372,    2, 0x08 /* Private */,
      57,    2,  373,    2, 0x08 /* Private */,
      60,    0,  378,    2, 0x08 /* Private */,
      61,    0,  379,    2, 0x08 /* Private */,
      62,    0,  380,    2, 0x08 /* Private */,
      63,    0,  381,    2, 0x08 /* Private */,
      64,    0,  382,    2, 0x08 /* Private */,
      65,    0,  383,    2, 0x08 /* Private */,
      66,    0,  384,    2, 0x08 /* Private */,
      67,    0,  385,    2, 0x08 /* Private */,
      68,    0,  386,    2, 0x08 /* Private */,
      69,    0,  387,    2, 0x08 /* Private */,
      70,    0,  388,    2, 0x08 /* Private */,
      71,    1,  389,    2, 0x08 /* Private */,
      72,    0,  392,    2, 0x08 /* Private */,
      73,    1,  393,    2, 0x08 /* Private */,

 // signals: parameters
    QMetaType::Void,
    QMetaType::Void,

 // slots: parameters
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void, QMetaType::Int,    7,
    QMetaType::Void,
    QMetaType::Void, QMetaType::Int,   10,
    QMetaType::Bool,
    QMetaType::Bool,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void, QMetaType::Bool,   18,
    QMetaType::Void, QMetaType::Bool,   18,
    QMetaType::Void, QMetaType::Bool,   21,
    QMetaType::Void, QMetaType::Int,    7,
    QMetaType::Void,
    QMetaType::Void, QMetaType::QString,   25,
    QMetaType::Void, QMetaType::QString,   27,
    QMetaType::Void, QMetaType::QString,   29,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void, QMetaType::Int,   35,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void, QMetaType::Double,   35,
    QMetaType::Void, 0x80000000 | 42,   43,
    QMetaType::Void, 0x80000000 | 45,   46,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void, 0x80000000 | 58, QMetaType::Int,   43,   59,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void, 0x80000000 | 42,   43,
    QMetaType::Void,
    QMetaType::Void, QMetaType::Int,    7,

       0        // eod
};

void moveit_rviz_plugin::MotionPlanningFrame::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    if (_c == QMetaObject::InvokeMetaMethod) {
        MotionPlanningFrame *_t = static_cast<MotionPlanningFrame *>(_o);
        Q_UNUSED(_t)
        switch (_id) {
        case 0: _t->planningFinished(); break;
        case 1: _t->configChanged(); break;
        case 2: _t->databaseConnectButtonClicked(); break;
        case 3: _t->publishSceneButtonClicked(); break;
        case 4: _t->planningAlgorithmIndexChanged((*reinterpret_cast< int(*)>(_a[1]))); break;
        case 5: _t->resetDbButtonClicked(); break;
        case 6: _t->approximateIKChanged((*reinterpret_cast< int(*)>(_a[1]))); break;
        case 7: { bool _r = _t->computeCartesianPlan();
            if (_a[0]) *reinterpret_cast< bool*>(_a[0]) = std::move(_r); }  break;
        case 8: { bool _r = _t->computeJointSpacePlan();
            if (_a[0]) *reinterpret_cast< bool*>(_a[0]) = std::move(_r); }  break;
        case 9: _t->planButtonClicked(); break;
        case 10: _t->executeButtonClicked(); break;
        case 11: _t->planAndExecuteButtonClicked(); break;
        case 12: _t->stopButtonClicked(); break;
        case 13: _t->allowReplanningToggled((*reinterpret_cast< bool(*)>(_a[1]))); break;
        case 14: _t->allowLookingToggled((*reinterpret_cast< bool(*)>(_a[1]))); break;
        case 15: _t->allowExternalProgramCommunication((*reinterpret_cast< bool(*)>(_a[1]))); break;
        case 16: _t->pathConstraintsIndexChanged((*reinterpret_cast< int(*)>(_a[1]))); break;
        case 17: _t->onNewPlanningSceneState(); break;
        case 18: _t->startStateTextChanged((*reinterpret_cast< const QString(*)>(_a[1]))); break;
        case 19: _t->goalStateTextChanged((*reinterpret_cast< const QString(*)>(_a[1]))); break;
        case 20: _t->planningGroupTextChanged((*reinterpret_cast< const QString(*)>(_a[1]))); break;
        case 21: _t->onClearOctomapClicked(); break;
        case 22: _t->importFileButtonClicked(); break;
        case 23: _t->importUrlButtonClicked(); break;
        case 24: _t->clearSceneButtonClicked(); break;
        case 25: _t->sceneScaleChanged((*reinterpret_cast< int(*)>(_a[1]))); break;
        case 26: _t->sceneScaleStartChange(); break;
        case 27: _t->sceneScaleEndChange(); break;
        case 28: _t->removeObjectButtonClicked(); break;
        case 29: _t->selectedCollisionObjectChanged(); break;
        case 30: _t->objectPoseValueChanged((*reinterpret_cast< double(*)>(_a[1]))); break;
        case 31: _t->collisionObjectChanged((*reinterpret_cast< QListWidgetItem*(*)>(_a[1]))); break;
        case 32: _t->imProcessFeedback((*reinterpret_cast< visualization_msgs::InteractiveMarkerFeedback(*)>(_a[1]))); break;
        case 33: _t->copySelectedCollisionObject(); break;
        case 34: _t->exportAsTextButtonClicked(); break;
        case 35: _t->importFromTextButtonClicked(); break;
        case 36: _t->saveSceneButtonClicked(); break;
        case 37: _t->planningSceneItemClicked(); break;
        case 38: _t->saveQueryButtonClicked(); break;
        case 39: _t->deleteSceneButtonClicked(); break;
        case 40: _t->deleteQueryButtonClicked(); break;
        case 41: _t->loadSceneButtonClicked(); break;
        case 42: _t->loadQueryButtonClicked(); break;
        case 43: _t->warehouseItemNameChanged((*reinterpret_cast< QTreeWidgetItem*(*)>(_a[1])),(*reinterpret_cast< int(*)>(_a[2]))); break;
        case 44: _t->loadStateButtonClicked(); break;
        case 45: _t->saveStartStateButtonClicked(); break;
        case 46: _t->saveGoalStateButtonClicked(); break;
        case 47: _t->removeStateButtonClicked(); break;
        case 48: _t->clearStatesButtonClicked(); break;
        case 49: _t->setAsStartStateButtonClicked(); break;
        case 50: _t->setAsGoalStateButtonClicked(); break;
        case 51: _t->detectObjectsButtonClicked(); break;
        case 52: _t->pickObjectButtonClicked(); break;
        case 53: _t->placeObjectButtonClicked(); break;
        case 54: _t->selectedDetectedObjectChanged(); break;
        case 55: _t->detectedObjectChanged((*reinterpret_cast< QListWidgetItem*(*)>(_a[1]))); break;
        case 56: _t->selectedSupportSurfaceChanged(); break;
        case 57: _t->tabChanged((*reinterpret_cast< int(*)>(_a[1]))); break;
        default: ;
        }
    } else if (_c == QMetaObject::IndexOfMethod) {
        int *result = reinterpret_cast<int *>(_a[0]);
        {
            typedef void (MotionPlanningFrame::*_t)();
            if (*reinterpret_cast<_t *>(_a[1]) == static_cast<_t>(&MotionPlanningFrame::planningFinished)) {
                *result = 0;
                return;
            }
        }
        {
            typedef void (MotionPlanningFrame::*_t)();
            if (*reinterpret_cast<_t *>(_a[1]) == static_cast<_t>(&MotionPlanningFrame::configChanged)) {
                *result = 1;
                return;
            }
        }
    }
}

const QMetaObject moveit_rviz_plugin::MotionPlanningFrame::staticMetaObject = {
    { &QWidget::staticMetaObject, qt_meta_stringdata_moveit_rviz_plugin__MotionPlanningFrame.data,
      qt_meta_data_moveit_rviz_plugin__MotionPlanningFrame,  qt_static_metacall, nullptr, nullptr}
};


const QMetaObject *moveit_rviz_plugin::MotionPlanningFrame::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *moveit_rviz_plugin::MotionPlanningFrame::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_meta_stringdata_moveit_rviz_plugin__MotionPlanningFrame.stringdata0))
        return static_cast<void*>(this);
    return QWidget::qt_metacast(_clname);
}

int moveit_rviz_plugin::MotionPlanningFrame::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QWidget::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    if (_c == QMetaObject::InvokeMetaMethod) {
        if (_id < 58)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 58;
    } else if (_c == QMetaObject::RegisterMethodArgumentMetaType) {
        if (_id < 58)
            *reinterpret_cast<int*>(_a[0]) = -1;
        _id -= 58;
    }
    return _id;
}

// SIGNAL 0
void moveit_rviz_plugin::MotionPlanningFrame::planningFinished()
{
    QMetaObject::activate(this, &staticMetaObject, 0, nullptr);
}

// SIGNAL 1
void moveit_rviz_plugin::MotionPlanningFrame::configChanged()
{
    QMetaObject::activate(this, &staticMetaObject, 1, nullptr);
}
QT_WARNING_POP
QT_END_MOC_NAMESPACE
