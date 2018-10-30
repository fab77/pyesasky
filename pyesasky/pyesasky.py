import ipywidgets as widgets
from traitlets import Unicode, default, Float
#from docutils.nodes import target
#from statsmodels.tsa.statespace.tests.test_mlemodel import kwargs
from .catalogue import Catalogue
from .footprintSet import FootprintSet
from .footprintSetDescriptor import FootprintSetDescriptor
from .metadataDescriptor import MetadataDescriptor
from .metadataType import MetadataType
from .HiPS import HiPS
import csv


__all__ = ['ESASkyWidget']


    
class ESASkyWidget(widgets.DOMWidget):

    _view_name = Unicode('ESASkyJSView').tag(sync=True)
    _model_name = Unicode('ESASkyJSModel').tag(sync=True)
    _view_module = Unicode('pyesasky').tag(sync=True)
    _model_module = Unicode('pyesasky').tag(sync=True)
    _view_module_version = Unicode('0.1.0').tag(sync=True)
    _model_module_version = Unicode('0.1.0').tag(sync=True)
    
    _targetname = Unicode('Mkr432').tag(sync=True)
    _fovDeg = Float(60).tag(sync=True)
    _colorPalette = Unicode('NATIVE').tag(sync=True)
    
    
    @default('layout')
    def _default_layout(self):
        return widgets.Layout(height='400px', align_self='stretch')


    def setGoToRADec(self, ra, dec):
        content = dict(
                       event='goToRADec',
                       ra=ra,
                       dec=dec
                )
        self.send(content)

    def goToTargetName(self, targetname):
        self._targetname = targetname 
        
    def setFoV(self, fovDeg):
        self._fovDeg = fovDeg
        
    def setHiPSColorPalette(self, colorPalette):
        self._colorPalette = colorPalette
        
    def overlayCatalogue(self, catalogue):
        
        content = dict(
                       event='overlayCatalogue',
                       content=catalogue.toDict()
                       )
        self.send(content)
        
    def clearCatalogue(self, catalogueName):
        content = dict(
                        event='clearCatalogue',
                       content=catalogueName
                        )
        self.send(content)

    def removeCatalogue(self, catalogueName):
        content = dict(
                        event='removeCatalogue',
                       content=catalogueName
                        )
        self.send(content)
    
    def clearFootprintsOverlay(self, overlayName):
        content = dict(
                        event='clearFootprintsOverlay',
                       content=overlayName
                        )
        self.send(content)

    def removeFootprintsOverlay(self, overlayName):
        content = dict(
                        event='removeFootprintsOverlay',
                       content=overlayName
                        )
        self.send(content)

    def setHiPS(self, hipsName, hipsURL, cooFrame, maxNorder, imgFormat):
        userHiPS = HiPS(hipsName, hipsURL, cooFrame, maxNorder, imgFormat)
        content = dict(
                       event='changeHiPS',
                       content=userHiPS.toDict()
                       )
        self.send(content)
    
    def overlayFootprints(self, footprintSet):
        content = dict(
                        event='overlayFootprints',
                       content=footprintSet.toDict()
                        )
        self.send(content)

    def overlayFootprintsWithDetails(self, footprintSet):
        content = dict(
                        event='overlayFootprintsWithDetails',
                       content=footprintSet.toDict()
                        )
        self.send(content)

    def overlayFootprintsFromCSV(self, pathToFile, csvDelimiter, footprintSetDescriptor):

        footprintSet = FootprintSet(footprintSetDescriptor.getDatasetName(), 'J2000', footprintSetDescriptor.getHistoColor(), footprintSetDescriptor.getLineWidth())

        #read colums
        with open(pathToFile) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=csvDelimiter)
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    columns = row
                    print(f'Column identified: {", ".join(row)}')
                    line_count += 1
                    i = 0
                    while i < len(columns):
                        if columns[i] == footprintSetDescriptor.getIdColumnName():
                            columnId = columns[i]
                            print('{id} column identified: '+columnId)
                            if footprintSetDescriptor.getIdColumnName() == footprintSetDescriptor.getNameColumnName():
                                columnName = columnId
                                print('{name} column identified: '+columnName)
                        elif columns[i] == footprintSetDescriptor.getNameColumnName():
                            columnName = columns[i]
                            print('{name} column identified: '+columnName)
                        elif columns[i] == footprintSetDescriptor.getStcsColumnName():
                            columnStcs = columns[i]
                            print('{stcs} column identified: '+columnStcs)
                        elif columns[i] == footprintSetDescriptor.getCentralRADegColumnName():
                            columnRaDeg = columns[i]
                            print('{centerRaDeg} column identified: '+columnRaDeg)
                        elif columns[i] == footprintSetDescriptor.getCentralDecDegColumnName():
                            columnDecDeg = columns[i]
                            print('{currDecDeg} column identified: '+columnDecDeg)
                        i += 1
                else:
                    i = 0
                    currDetails = []
                    currId = ''
                    currName = ''
                    currStcs = ''
                    currRaDeg = ''
                    currDecDeg = ''

                    while i < len(row):
                        if columns[i] == footprintSetDescriptor.getIdColumnName():
                            currId = row[i]
                            if footprintSetDescriptor.getIdColumnName() == footprintSetDescriptor.getNameColumnName():
                                currName = currId
                        elif columns[i] == footprintSetDescriptor.getNameColumnName():
                            currName = row[i]
                        elif columns[i] == footprintSetDescriptor.getStcsColumnName():
                            currStcs = row[i]
                        elif columns[i] == footprintSetDescriptor.getCentralRADegColumnName():
                            currRaDeg = row[i]
                        elif columns[i] == footprintSetDescriptor.getCentralDecDegColumnName():
                            currDecDeg = row[i]
                        else:
                            currMetadata = {}
                            if len(footprintSetDescriptor.getMetadata()) > 0:
                                j = 0
                                while j < len(footprintSetDescriptor.getMetadata()):
                                    if footprintSetDescriptor.getMetadata()[j].getLabel() == columns[i]:
                                        currMetadata['name'] = footprintSetDescriptor.getMetadata()[j].getLabel()
                                        currMetadata['value'] = row[i]
                                        currMetadata['type'] = footprintSetDescriptor.getMetadata()[j].getType()
                                        #currMetadata = {
                                        #    'name': footprintSetDescriptor.getMetadata()[j].getLabel(),
                                        #    'value': row[i],
                                        #    'type': footprintSetDescriptor.getMetadata()[j].getType()
                                        #    }
                                        break
                                    j += 1
                            else:
                                currMetadata['name'] = columns[i]
                                currMetadata['value'] = row[i]
                                currMetadata['type'] = MetadataType.STRING
                                #currMetadata = {
                                #    'name': columns[i],
                                #    'value': row[i],
                                #    'type': MetadataType.STRING
                                #    }
                            currDetails.append(currMetadata)

                        i += 1
                    #print ('Adding footprint (id:'+currId+', name:'+currName+', raDeg:'+currRaDeg+', decDeg:'+currDecDeg+', stcs:'+currStcs)
                    #k = 0
                    #while k < len(currDetails):
                    #    print ('\t (name:'+currDetails[k]['name']+', type:'+currDetails[k]['type']+', value:'+currDetails[k]['value'])
                    #    k += 1
                    
                    footprintSet.addFootprint(currName, currStcs, currId, currRaDeg, currDecDeg, currDetails)
                    #print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
                    line_count += 1
            print(f'Processed {line_count} lines.')
            self.overlayFootprintsWithDetails(footprintSet)


    def overlayCatalogueFromAstropyTable(self, catalogueName, cooFrame, color, table, raColName, decColName, mainIdColName):
        
        raColNameUserInput = True
        decColNameUserInput = True
        mainIdColNameUserInput = True
        
        if not raColName:
            raColName = ''
            raColNameUserInput = False
        
        if not decColName:
            decColName = ''
            decColNameUserInput = False
            
        if not mainIdColName:
            mainIdColName = ''
            mainIdColNameUserInput = False
        
        i = 0
        #columnNames = []
        #columnTypes = []

        if (not raColNameUserInput and not decColNameUserInput and not mainIdColNameUserInput):
             
            while i < len(table.colnames):
                
                colName = table.colnames[i]
                #columnNames[i] = colName
                #columnTypes[i] = 

                if len(table[colName].meta) > 0:
                    metaType = table[colName].meta['ucd']
                    print('-----------')
                    print(colName)
                    print(metaType)
                    if ('pos.eq.ra;meta.main' in metaType and not raColNameUserInput):
                        raColName = colName
                    elif ('pos.eq.dec;meta.main' in metaType and not decColNameUserInput):
                        decColName = colName
                    elif ('meta.id;meta.main' in metaType and not mainIdColNameUserInput):
                        mainIdColName = colName 
                i += 1
        
        userCatalogue = Catalogue(catalogueName, cooFrame, color, 10)
        
        j = 0
        while j < len(table):
            raValue = table[j][raColName]
            decValue = table[j][decColName]
            
            nameValue = table[j][mainIdColName]
            if type(nameValue) == 'byte':
                nameValue = nameValue.decode('utf-8')
            elif type(nameValue) != 'str':
                nameValue = str(nameValue)
            #print ('name '+ table[j][mainIdColName] +' ra '+table[j][raColName] +' dec '+ table[j][decColName])
            #userCatalogue.addSource((table[j][mainIdColName]).decode('utf-8'), table[j][raColName], table[j][decColName])

            #while k < len(table.colnames):
            #    metadata[k] = table[j][table.colnames[k]]    
            #    k += 1

            userCatalogue.addSource(nameValue, raValue, decValue)
            j += 1
        
        self.overlayCatalogue(userCatalogue)

        
        
