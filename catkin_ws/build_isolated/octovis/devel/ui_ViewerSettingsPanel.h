/********************************************************************************
** Form generated from reading UI file 'ViewerSettingsPanel.ui'
**
** Created by: Qt User Interface Compiler version 5.9.5
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_VIEWERSETTINGSPANEL_H
#define UI_VIEWERSETTINGSPANEL_H

#include <QtCore/QVariant>
#include <QtWidgets/QAction>
#include <QtWidgets/QApplication>
#include <QtWidgets/QButtonGroup>
#include <QtWidgets/QFormLayout>
#include <QtWidgets/QGridLayout>
#include <QtWidgets/QGroupBox>
#include <QtWidgets/QHBoxLayout>
#include <QtWidgets/QHeaderView>
#include <QtWidgets/QLabel>
#include <QtWidgets/QProgressBar>
#include <QtWidgets/QSlider>
#include <QtWidgets/QSpinBox>
#include <QtWidgets/QToolButton>
#include <QtWidgets/QVBoxLayout>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_ViewerSettingsPanelClass
{
public:
    QVBoxLayout *verticalLayout_2;
    QGroupBox *groupBox_2;
    QVBoxLayout *verticalLayout_3;
    QGridLayout *gridLayout;
    QSpinBox *treeDepth;
    QSlider *treeDepthSlider;
    QFormLayout *formLayout;
    QLabel *leafSizeLabel;
    QLabel *leafSize;
    QGroupBox *groupBox;
    QVBoxLayout *verticalLayout_5;
    QHBoxLayout *horizontalLayout;
    QToolButton *firstScanButton;
    QToolButton *nextScanButton;
    QToolButton *fastFwdScanButton;
    QToolButton *lastScanButton;
    QVBoxLayout *verticalLayout_4;
    QProgressBar *scanProgressBar;

    void setupUi(QWidget *ViewerSettingsPanelClass)
    {
        if (ViewerSettingsPanelClass->objectName().isEmpty())
            ViewerSettingsPanelClass->setObjectName(QStringLiteral("ViewerSettingsPanelClass"));
        ViewerSettingsPanelClass->resize(347, 479);
        QSizePolicy sizePolicy(QSizePolicy::Preferred, QSizePolicy::Preferred);
        sizePolicy.setHorizontalStretch(0);
        sizePolicy.setVerticalStretch(0);
        sizePolicy.setHeightForWidth(ViewerSettingsPanelClass->sizePolicy().hasHeightForWidth());
        ViewerSettingsPanelClass->setSizePolicy(sizePolicy);
        verticalLayout_2 = new QVBoxLayout(ViewerSettingsPanelClass);
        verticalLayout_2->setSpacing(6);
        verticalLayout_2->setContentsMargins(11, 11, 11, 11);
        verticalLayout_2->setObjectName(QStringLiteral("verticalLayout_2"));
        groupBox_2 = new QGroupBox(ViewerSettingsPanelClass);
        groupBox_2->setObjectName(QStringLiteral("groupBox_2"));
        QSizePolicy sizePolicy1(QSizePolicy::Minimum, QSizePolicy::MinimumExpanding);
        sizePolicy1.setHorizontalStretch(0);
        sizePolicy1.setVerticalStretch(0);
        sizePolicy1.setHeightForWidth(groupBox_2->sizePolicy().hasHeightForWidth());
        groupBox_2->setSizePolicy(sizePolicy1);
        groupBox_2->setAlignment(Qt::AlignHCenter|Qt::AlignTop);
        groupBox_2->setFlat(false);
        groupBox_2->setCheckable(false);
        verticalLayout_3 = new QVBoxLayout(groupBox_2);
        verticalLayout_3->setSpacing(6);
        verticalLayout_3->setContentsMargins(11, 11, 11, 11);
        verticalLayout_3->setObjectName(QStringLiteral("verticalLayout_3"));
        gridLayout = new QGridLayout();
        gridLayout->setSpacing(6);
        gridLayout->setObjectName(QStringLiteral("gridLayout"));
        treeDepth = new QSpinBox(groupBox_2);
        treeDepth->setObjectName(QStringLiteral("treeDepth"));
        treeDepth->setMinimumSize(QSize(4, 0));
        treeDepth->setMaximumSize(QSize(16777196, 16777215));
        treeDepth->setReadOnly(false);
        treeDepth->setButtonSymbols(QAbstractSpinBox::NoButtons);
        treeDepth->setMinimum(1);
        treeDepth->setMaximum(16);
        treeDepth->setValue(16);

        gridLayout->addWidget(treeDepth, 0, 0, 1, 1);

        treeDepthSlider = new QSlider(groupBox_2);
        treeDepthSlider->setObjectName(QStringLiteral("treeDepthSlider"));
        treeDepthSlider->setMinimumSize(QSize(0, 75));
        treeDepthSlider->setMaximumSize(QSize(16777215, 500));
        treeDepthSlider->setMinimum(1);
        treeDepthSlider->setMaximum(16);
        treeDepthSlider->setPageStep(1);
        treeDepthSlider->setValue(16);
        treeDepthSlider->setOrientation(Qt::Vertical);
        treeDepthSlider->setInvertedAppearance(true);
        treeDepthSlider->setInvertedControls(true);
        treeDepthSlider->setTickPosition(QSlider::TicksBothSides);
        treeDepthSlider->setTickInterval(1);

        gridLayout->addWidget(treeDepthSlider, 1, 0, 1, 1);


        verticalLayout_3->addLayout(gridLayout);

        formLayout = new QFormLayout();
        formLayout->setSpacing(6);
        formLayout->setObjectName(QStringLiteral("formLayout"));
        formLayout->setSizeConstraint(QLayout::SetMinimumSize);
        leafSizeLabel = new QLabel(groupBox_2);
        leafSizeLabel->setObjectName(QStringLiteral("leafSizeLabel"));

        formLayout->setWidget(0, QFormLayout::LabelRole, leafSizeLabel);

        leafSize = new QLabel(groupBox_2);
        leafSize->setObjectName(QStringLiteral("leafSize"));
        leafSize->setTextFormat(Qt::PlainText);

        formLayout->setWidget(0, QFormLayout::FieldRole, leafSize);


        verticalLayout_3->addLayout(formLayout);


        verticalLayout_2->addWidget(groupBox_2);

        groupBox = new QGroupBox(ViewerSettingsPanelClass);
        groupBox->setObjectName(QStringLiteral("groupBox"));
        verticalLayout_5 = new QVBoxLayout(groupBox);
        verticalLayout_5->setSpacing(6);
        verticalLayout_5->setContentsMargins(11, 11, 11, 11);
        verticalLayout_5->setObjectName(QStringLiteral("verticalLayout_5"));
        horizontalLayout = new QHBoxLayout();
        horizontalLayout->setSpacing(6);
        horizontalLayout->setObjectName(QStringLiteral("horizontalLayout"));
        firstScanButton = new QToolButton(groupBox);
        firstScanButton->setObjectName(QStringLiteral("firstScanButton"));
        QIcon icon;
        icon.addFile(QStringLiteral(":/icons/media-skip-backward.png"), QSize(), QIcon::Normal, QIcon::Off);
        firstScanButton->setIcon(icon);

        horizontalLayout->addWidget(firstScanButton);

        nextScanButton = new QToolButton(groupBox);
        nextScanButton->setObjectName(QStringLiteral("nextScanButton"));
        QIcon icon1;
        icon1.addFile(QStringLiteral(":/icons/media-playback-start.png"), QSize(), QIcon::Normal, QIcon::Off);
        nextScanButton->setIcon(icon1);

        horizontalLayout->addWidget(nextScanButton);

        fastFwdScanButton = new QToolButton(groupBox);
        fastFwdScanButton->setObjectName(QStringLiteral("fastFwdScanButton"));
        QIcon icon2;
        icon2.addFile(QStringLiteral(":/icons/media-seek-forward.png"), QSize(), QIcon::Normal, QIcon::Off);
        fastFwdScanButton->setIcon(icon2);

        horizontalLayout->addWidget(fastFwdScanButton);

        lastScanButton = new QToolButton(groupBox);
        lastScanButton->setObjectName(QStringLiteral("lastScanButton"));
        QIcon icon3;
        icon3.addFile(QStringLiteral(":/icons/media-skip-forward.png"), QSize(), QIcon::Normal, QIcon::Off);
        lastScanButton->setIcon(icon3);

        horizontalLayout->addWidget(lastScanButton);


        verticalLayout_5->addLayout(horizontalLayout);

        verticalLayout_4 = new QVBoxLayout();
        verticalLayout_4->setSpacing(6);
        verticalLayout_4->setObjectName(QStringLiteral("verticalLayout_4"));
        scanProgressBar = new QProgressBar(groupBox);
        scanProgressBar->setObjectName(QStringLiteral("scanProgressBar"));
        scanProgressBar->setValue(24);
        scanProgressBar->setTextVisible(true);
        scanProgressBar->setInvertedAppearance(false);

        verticalLayout_4->addWidget(scanProgressBar);


        verticalLayout_5->addLayout(verticalLayout_4);


        verticalLayout_2->addWidget(groupBox);


        retranslateUi(ViewerSettingsPanelClass);
        QObject::connect(treeDepthSlider, SIGNAL(sliderMoved(int)), treeDepth, SLOT(setValue(int)));
        QObject::connect(treeDepth, SIGNAL(valueChanged(int)), treeDepthSlider, SLOT(setValue(int)));

        QMetaObject::connectSlotsByName(ViewerSettingsPanelClass);
    } // setupUi

    void retranslateUi(QWidget *ViewerSettingsPanelClass)
    {
        ViewerSettingsPanelClass->setWindowTitle(QApplication::translate("ViewerSettingsPanelClass", "ViewerSettingsPanel", Q_NULLPTR));
        groupBox_2->setTitle(QApplication::translate("ViewerSettingsPanelClass", "Tree depth cutoff", Q_NULLPTR));
        leafSizeLabel->setText(QApplication::translate("ViewerSettingsPanelClass", "Leaf size:", Q_NULLPTR));
        leafSize->setText(QApplication::translate("ViewerSettingsPanelClass", "0 m", Q_NULLPTR));
        groupBox->setTitle(QApplication::translate("ViewerSettingsPanelClass", "Scan graph progress", Q_NULLPTR));
#ifndef QT_NO_TOOLTIP
        firstScanButton->setToolTip(QApplication::translate("ViewerSettingsPanelClass", "first scan", Q_NULLPTR));
#endif // QT_NO_TOOLTIP
        firstScanButton->setText(QApplication::translate("ViewerSettingsPanelClass", "first scan", Q_NULLPTR));
#ifndef QT_NO_TOOLTIP
        nextScanButton->setToolTip(QApplication::translate("ViewerSettingsPanelClass", "next scan", Q_NULLPTR));
#endif // QT_NO_TOOLTIP
        nextScanButton->setText(QApplication::translate("ViewerSettingsPanelClass", "next scan", Q_NULLPTR));
#ifndef QT_NO_TOOLTIP
        fastFwdScanButton->setToolTip(QApplication::translate("ViewerSettingsPanelClass", "next 5 scans", Q_NULLPTR));
#endif // QT_NO_TOOLTIP
        fastFwdScanButton->setText(QApplication::translate("ViewerSettingsPanelClass", "next 5 scans", Q_NULLPTR));
#ifndef QT_NO_TOOLTIP
        lastScanButton->setToolTip(QApplication::translate("ViewerSettingsPanelClass", "last scan", Q_NULLPTR));
#endif // QT_NO_TOOLTIP
        lastScanButton->setText(QApplication::translate("ViewerSettingsPanelClass", "last scan", Q_NULLPTR));
        scanProgressBar->setFormat(QApplication::translate("ViewerSettingsPanelClass", "%v/%m", Q_NULLPTR));
    } // retranslateUi

};

namespace Ui {
    class ViewerSettingsPanelClass: public Ui_ViewerSettingsPanelClass {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_VIEWERSETTINGSPANEL_H
