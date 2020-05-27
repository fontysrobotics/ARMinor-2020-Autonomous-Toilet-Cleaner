/********************************************************************************
** Form generated from reading UI file 'ViewerSettings.ui'
**
** Created by: Qt User Interface Compiler version 5.9.5
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_VIEWERSETTINGS_H
#define UI_VIEWERSETTINGS_H

#include <QtCore/QVariant>
#include <QtWidgets/QAction>
#include <QtWidgets/QApplication>
#include <QtWidgets/QButtonGroup>
#include <QtWidgets/QComboBox>
#include <QtWidgets/QDialog>
#include <QtWidgets/QDialogButtonBox>
#include <QtWidgets/QDoubleSpinBox>
#include <QtWidgets/QFormLayout>
#include <QtWidgets/QHeaderView>
#include <QtWidgets/QLabel>
#include <QtWidgets/QVBoxLayout>

QT_BEGIN_NAMESPACE

class Ui_ViewerSettingsClass
{
public:
    QVBoxLayout *verticalLayout;
    QFormLayout *formLayout;
    QLabel *label;
    QDoubleSpinBox *resolution;
    QComboBox *laserType;
    QLabel *label_2;
    QLabel *label_3;
    QDoubleSpinBox *maxRange;
    QDialogButtonBox *buttonBox;

    void setupUi(QDialog *ViewerSettingsClass)
    {
        if (ViewerSettingsClass->objectName().isEmpty())
            ViewerSettingsClass->setObjectName(QStringLiteral("ViewerSettingsClass"));
        ViewerSettingsClass->resize(400, 201);
        verticalLayout = new QVBoxLayout(ViewerSettingsClass);
        verticalLayout->setSpacing(6);
        verticalLayout->setContentsMargins(11, 11, 11, 11);
        verticalLayout->setObjectName(QStringLiteral("verticalLayout"));
        formLayout = new QFormLayout();
        formLayout->setSpacing(6);
        formLayout->setObjectName(QStringLiteral("formLayout"));
        formLayout->setFieldGrowthPolicy(QFormLayout::AllNonFixedFieldsGrow);
        label = new QLabel(ViewerSettingsClass);
        label->setObjectName(QStringLiteral("label"));

        formLayout->setWidget(0, QFormLayout::LabelRole, label);

        resolution = new QDoubleSpinBox(ViewerSettingsClass);
        resolution->setObjectName(QStringLiteral("resolution"));
        resolution->setDecimals(3);
        resolution->setSingleStep(0.001);
        resolution->setValue(0.1);

        formLayout->setWidget(2, QFormLayout::FieldRole, resolution);

        laserType = new QComboBox(ViewerSettingsClass);
        laserType->setObjectName(QStringLiteral("laserType"));

        formLayout->setWidget(0, QFormLayout::FieldRole, laserType);

        label_2 = new QLabel(ViewerSettingsClass);
        label_2->setObjectName(QStringLiteral("label_2"));

        formLayout->setWidget(2, QFormLayout::LabelRole, label_2);

        label_3 = new QLabel(ViewerSettingsClass);
        label_3->setObjectName(QStringLiteral("label_3"));

        formLayout->setWidget(1, QFormLayout::LabelRole, label_3);

        maxRange = new QDoubleSpinBox(ViewerSettingsClass);
        maxRange->setObjectName(QStringLiteral("maxRange"));
        maxRange->setMinimum(-1);
        maxRange->setMaximum(1000);
        maxRange->setSingleStep(0.1);
        maxRange->setValue(-1);

        formLayout->setWidget(1, QFormLayout::FieldRole, maxRange);


        verticalLayout->addLayout(formLayout);

        buttonBox = new QDialogButtonBox(ViewerSettingsClass);
        buttonBox->setObjectName(QStringLiteral("buttonBox"));
        buttonBox->setStandardButtons(QDialogButtonBox::Cancel|QDialogButtonBox::Ok);

        verticalLayout->addWidget(buttonBox);

#ifndef QT_NO_SHORTCUT
        label->setBuddy(laserType);
        label_2->setBuddy(resolution);
#endif // QT_NO_SHORTCUT

        retranslateUi(ViewerSettingsClass);
        QObject::connect(buttonBox, SIGNAL(accepted()), ViewerSettingsClass, SLOT(accept()));
        QObject::connect(buttonBox, SIGNAL(rejected()), ViewerSettingsClass, SLOT(reject()));

        QMetaObject::connectSlotsByName(ViewerSettingsClass);
    } // setupUi

    void retranslateUi(QDialog *ViewerSettingsClass)
    {
        ViewerSettingsClass->setWindowTitle(QApplication::translate("ViewerSettingsClass", "ViewerSettings", Q_NULLPTR));
        label->setText(QApplication::translate("ViewerSettingsClass", "Laser type: ", Q_NULLPTR));
        laserType->clear();
        laserType->insertItems(0, QStringList()
         << QApplication::translate("ViewerSettingsClass", "Hokuyo URG", Q_NULLPTR)
         << QApplication::translate("ViewerSettingsClass", "Sick LMS", Q_NULLPTR)
        );
        label_2->setText(QApplication::translate("ViewerSettingsClass", "Octree resolution (m)", Q_NULLPTR));
        label_3->setText(QApplication::translate("ViewerSettingsClass", "Max. laser range (m) -1: no limit", Q_NULLPTR));
    } // retranslateUi

};

namespace Ui {
    class ViewerSettingsClass: public Ui_ViewerSettingsClass {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_VIEWERSETTINGS_H
