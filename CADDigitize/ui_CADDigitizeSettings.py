# -*- coding: utf-8 -*-
"""
/***************************************************************************
 CADDigitize
                                 A QGIS plugin
 CAD like tools for QGis
 Fork of Rectangles Ovals Digitizing. Inspired by CadTools, LibreCAD/AutoCAD.
                              -------------------
        begin                : 2014-08-11
        git sha              : $Format:%H$
        copyright            : (C) 2014 by Loïc BARTOLETTI
        email                : l.bartoletti@free.fr
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

# Form implementation generated from reading ui file 'ui_CADDigitizeSettings.ui'
#
# Created: Tue Oct 28 07:00:18 2014
#      by: PyQt4 UI code generator 4.11.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_CADDigitizeSettings(object):
    def setupUi(self, CADDigitizeSettings):
        CADDigitizeSettings.setObjectName(_fromUtf8("CADDigitizeSettings"))
        CADDigitizeSettings.resize(515, 500)
        self.verticalLayout_6 = QtGui.QVBoxLayout(CADDigitizeSettings)
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.tabWidget = QtGui.QTabWidget(CADDigitizeSettings)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.CircleTab = QtGui.QWidget()
        self.CircleTab.setObjectName(_fromUtf8("CircleTab"))
        self.layoutWidget = QtGui.QWidget(self.CircleTab)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 20, 134, 39))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_5.setMargin(0)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.label_2 = QtGui.QLabel(self.layoutWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout_5.addWidget(self.label_2)
        self.circleSegmentsSpinbox = QtGui.QDoubleSpinBox(self.layoutWidget)
        self.circleSegmentsSpinbox.setDecimals(0)
        self.circleSegmentsSpinbox.setMinimum(4.0)
        self.circleSegmentsSpinbox.setMaximum(3600.0)
        self.circleSegmentsSpinbox.setProperty("value", 8.0)
        self.circleSegmentsSpinbox.setObjectName(_fromUtf8("circleSegmentsSpinbox"))
        self.verticalLayout_5.addWidget(self.circleSegmentsSpinbox)
        self.tabWidget.addTab(self.CircleTab, _fromUtf8(""))
        self.EllipseTab = QtGui.QWidget()
        self.EllipseTab.setObjectName(_fromUtf8("EllipseTab"))
        self.layoutWidget1 = QtGui.QWidget(self.EllipseTab)
        self.layoutWidget1.setGeometry(QtCore.QRect(10, 20, 134, 39))
        self.layoutWidget1.setObjectName(_fromUtf8("layoutWidget1"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_4.setMargin(0)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.label = QtGui.QLabel(self.layoutWidget1)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout_4.addWidget(self.label)
        self.ellipsePointsSpinbox = QtGui.QDoubleSpinBox(self.layoutWidget1)
        self.ellipsePointsSpinbox.setDecimals(0)
        self.ellipsePointsSpinbox.setMinimum(4.0)
        self.ellipsePointsSpinbox.setMaximum(3600.0)
        self.ellipsePointsSpinbox.setProperty("value", 8.0)
        self.ellipsePointsSpinbox.setObjectName(_fromUtf8("ellipsePointsSpinbox"))
        self.verticalLayout_4.addWidget(self.ellipsePointsSpinbox)
        self.tabWidget.addTab(self.EllipseTab, _fromUtf8(""))
        self.ArcTab = QtGui.QWidget()
        self.ArcTab.setObjectName(_fromUtf8("ArcTab"))
        self.layoutWidget2 = QtGui.QWidget(self.ArcTab)
        self.layoutWidget2.setGeometry(QtCore.QRect(11, 11, 461, 391))
        self.layoutWidget2.setObjectName(_fromUtf8("layoutWidget2"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_3.setMargin(0)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.groupBox = QtGui.QGroupBox(self.layoutWidget2)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout_8 = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout_8.setObjectName(_fromUtf8("verticalLayout_8"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.radioFeatureAngle = QtGui.QRadioButton(self.groupBox)
        self.radioFeatureAngle.setObjectName(_fromUtf8("radioFeatureAngle"))
        self.horizontalLayout_2.addWidget(self.radioFeatureAngle)
        self.ArcFeatureAngle = QtGui.QDoubleSpinBox(self.groupBox)
        self.ArcFeatureAngle.setDecimals(1)
        self.ArcFeatureAngle.setProperty("value", 1.0)
        self.ArcFeatureAngle.setObjectName(_fromUtf8("ArcFeatureAngle"))
        self.horizontalLayout_2.addWidget(self.ArcFeatureAngle)
        self.verticalLayout_8.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.radioFeaturePitch = QtGui.QRadioButton(self.groupBox)
        self.radioFeaturePitch.setChecked(True)
        self.radioFeaturePitch.setObjectName(_fromUtf8("radioFeaturePitch"))
        self.horizontalLayout.addWidget(self.radioFeaturePitch)
        self.ArcFeaturePitch = QtGui.QDoubleSpinBox(self.groupBox)
        self.ArcFeaturePitch.setEnabled(True)
        self.ArcFeaturePitch.setDecimals(1)
        self.ArcFeaturePitch.setMaximum(100.0)
        self.ArcFeaturePitch.setProperty("value", 2.0)
        self.ArcFeaturePitch.setObjectName(_fromUtf8("ArcFeaturePitch"))
        self.horizontalLayout.addWidget(self.ArcFeaturePitch)
        self.verticalLayout_8.addLayout(self.horizontalLayout)
        self.verticalLayout_3.addWidget(self.groupBox)
        self.groupBox_2 = QtGui.QGroupBox(self.layoutWidget2)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.layoutWidget3 = QtGui.QWidget(self.groupBox_2)
        self.layoutWidget3.setGeometry(QtCore.QRect(10, 20, 113, 40))
        self.layoutWidget3.setObjectName(_fromUtf8("layoutWidget3"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.layoutWidget3)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.ArcClockWise = QtGui.QRadioButton(self.layoutWidget3)
        self.ArcClockWise.setChecked(True)
        self.ArcClockWise.setObjectName(_fromUtf8("ArcClockWise"))
        self.verticalLayout_2.addWidget(self.ArcClockWise)
        self.ArcCounterClockWise = QtGui.QRadioButton(self.layoutWidget3)
        self.ArcCounterClockWise.setObjectName(_fromUtf8("ArcCounterClockWise"))
        self.verticalLayout_2.addWidget(self.ArcCounterClockWise)
        self.verticalLayout_3.addWidget(self.groupBox_2)
        self.groupBox_3 = QtGui.QGroupBox(self.layoutWidget2)
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.layoutWidget_2 = QtGui.QWidget(self.groupBox_3)
        self.layoutWidget_2.setGeometry(QtCore.QRect(10, 20, 113, 40))
        self.layoutWidget_2.setObjectName(_fromUtf8("layoutWidget_2"))
        self.verticalLayout_7 = QtGui.QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_7.setMargin(0)
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.ArcPolygonChord = QtGui.QRadioButton(self.layoutWidget_2)
        self.ArcPolygonChord.setChecked(True)
        self.ArcPolygonChord.setObjectName(_fromUtf8("ArcPolygonChord"))
        self.verticalLayout_7.addWidget(self.ArcPolygonChord)
        self.ArcPolygonPie = QtGui.QRadioButton(self.layoutWidget_2)
        self.ArcPolygonPie.setObjectName(_fromUtf8("ArcPolygonPie"))
        self.verticalLayout_7.addWidget(self.ArcPolygonPie)
        self.verticalLayout_3.addWidget(self.groupBox_3)
        self.tabWidget.addTab(self.ArcTab, _fromUtf8(""))
        self.verticalLayout.addWidget(self.tabWidget)
        self.buttonBox = QtGui.QDialogButtonBox(CADDigitizeSettings)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)
        self.verticalLayout_6.addLayout(self.verticalLayout)

        self.retranslateUi(CADDigitizeSettings)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), CADDigitizeSettings.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), CADDigitizeSettings.reject)
        QtCore.QMetaObject.connectSlotsByName(CADDigitizeSettings)

    def retranslateUi(self, CADDigitizeSettings):
        CADDigitizeSettings.setWindowTitle(_translate("CADDigitizeSettings", "CADDigitize Settings", None))
        self.label_2.setText(_translate("CADDigitizeSettings", "Quadrant segment", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.CircleTab), _translate("CADDigitizeSettings", "Circle", None))
        self.label.setText(_translate("CADDigitizeSettings", "Number of points on ellipse", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.EllipseTab), _translate("CADDigitizeSettings", "Ellipse", None))
        self.groupBox.setTitle(_translate("CADDigitizeSettings", "Feature Segmentation", None))
        self.radioFeatureAngle.setText(_translate("CADDigitizeSettings", "Angle", None))
        self.ArcFeatureAngle.setPrefix(_translate("CADDigitizeSettings", "Degree(s) ", None))
        self.radioFeaturePitch.setText(_translate("CADDigitizeSettings", "Pitch", None))
        self.ArcFeaturePitch.setPrefix(_translate("CADDigitizeSettings", "Millimeter(s) ", None))
        self.groupBox_2.setTitle(_translate("CADDigitizeSettings", "Angle Direction", None))
        self.ArcClockWise.setText(_translate("CADDigitizeSettings", "ClockWise", None))
        self.ArcCounterClockWise.setText(_translate("CADDigitizeSettings", "CounterClockWise", None))
        self.groupBox_3.setTitle(_translate("CADDigitizeSettings", "Polygon creation", None))
        self.ArcPolygonChord.setText(_translate("CADDigitizeSettings", "Chord", None))
        self.ArcPolygonPie.setText(_translate("CADDigitizeSettings", "Pie segment", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.ArcTab), _translate("CADDigitizeSettings", "Arcs", None))

