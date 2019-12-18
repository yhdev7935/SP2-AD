# DDS (Detailed Design Specification)

## Folder: GameMain

### Class:  GameMain.py
|메서드|입력 인자|입력 인자 타입|출력 인자|출력 인자 타입|기능|
|:--:|:--:|:--:|:--:|:--:|:--:|
| \_\_init\_\_ 생성자 |  |  |  |  | Loading 객체생성<br>DataManagement 객체생성<br>Client Lastest Version 불러오기<br>MapUploadConfirm 객체생성 |
| initClientID |  |  |  |  | Client ID이 존재하지 않으면 생성/갱신 |
| setStatus | msg | str |  |  | StatusBar 메시지 설정 |
| start |  |  |  |  | MainLayout를 show상태로 변경<br>버전 확인(self.showCheckVersion()) |
| changetoMapList |  |  |  |  | MapListLayout으로 MainLayout 교체 |
| changetoGameMainLayout |  |  |  |  | GameMainLayout으로 MainLayout 교체 |
| showCheckVersion |  |  |  |  | 버전이 깃허브에 업로드된 버전과 다른 경우 MessageBox 팝업 |
| quit |  |  |  |  | MainLayout 닫기 |
| hideWindow |  |  |  |  | MainLayout 숨김 |
| showWindow |  |  |  |  | MainLayout 나타냄 |

### Class:  GameMainButton.py
|메서드|입력 인자|입력 인자 타입|출력 인자|출력 인자 타입|기능|
|:--:|:--:|:--:|:--:|:--:|:--:|
| \_\_init\_\_ 생성자 | text, GameMain | str, GameMain() |  |  | QPushButton 생성, 폰트 설정 |
| \_\_str\_\_ |  |  | self | GameMainButton() | return 객체 자신 |
| buttonClicked |  |  |  |  | 클릭된 버튼에 따라서 Call Event Method |
| onStartClick |  |  |  |  |  |
| onMapClick |  |  |  |  | 깃허브 버전과 동일한 경우 MapListLayout으로 MainLayout 교체<br>다른 경우 작동하지 않음 |
| onExitClick |  |  |  |  | MainLayout Close |


### Class:  GameMainLayout.py
|메서드|입력 인자|입력 인자 타입|출력 인자|출력 인자 타입|기능|
|:--:|:--:|:--:|:--:|:--:|:--:|
| \_\_init\_\_ 생성자 | GameMain | GameMain() |  |  | Layout Initialization |
| initUI |  |  |  |  | 기본 Widget과 Layout들을 적용(mainLayout)<br>인터넷이 연결안될 경우 Map Button Load하지 않음 |
| ClientDataLayout |  |  | ret | QVBoxLayout() | 제목, Client 버전, GitHub 버전 Layout |
| nameWidget |  |  | ret | QLabel() | 제목 Widget |
| makeButtonWidget | text | str | button | GameMainButton() | Button 내용이 text인 GameMainButton() return |
| makeButtonLayout | button | QPushButton() | layout | QHBoxLayout() | Buttons\' Layout 구성 |
| getMainLayout |  |  | self.mainLayout | QVBoxLayout() | mainLayout return |
| setStatus |  |  |  |  | StatusBar 설정 |

### Class:  Loading.py
|메서드|입력 인자|입력 인자 타입|출력 인자|출력 인자 타입|기능|
|:--:|:--:|:--:|:--:|:--:|:--:|
| \_\_init\_\_ 생성자 | GameMain | GameMain() |  |  | Layout Initialization<br>LoadingThread 객체생성 |
| initUI |  |  |  |  | 기본 UI 틀 작성/적용 |
| getMainLabelLayout |  |  | layout | QHBoxLayout() | Loading Label 구성 |
| getLoadingStatusLabelLayout |  |  | layout | QHBoxLayout() | Loading Status Label 구성 |
| setLoadingStatus | msg | str |  |  | LoadingStatus 설정<br>폰트 자동맞춤 |


### Class:  LoadingThread.py
|메서드|입력 인자|입력 인자 타입|출력 인자|출력 인자 타입|기능|
|:--:|:--:|:--:|:--:|:--:|:--:|
| \_\_init\_\_ 생성자 | GameMain, Loading | GameMain(), Loading() |  |  | QThread Initialization |
| run |  |  |  |  | 지속적으로 Loading Status 메시지 변경 |

## Folder: Data

### Class: FileDataManagement.py
|메서드|입력 인자|입력 인자 타입|출력 인자|출력 인자 타입|기능|
|:--:|:--:|:--:|:--:|:--:|:--:|
| \_\_init\_\_ 생성자 | file | str |  |  | 파일 경로에 파일이 존재하지 않으면 파일을 wb상태로 open |
| readFile |  |  | data | dict() | 파일을 읽어 pickle로 데이터 변환 |
| get | key | str | ret | str | readFile로 읽은 dict에서 value 추출 |
| set | key, value | str, value |  |  | readFile로 읽은 dict에서 key값에 따른 value집어넣기 |
| delete |  |  |  |  | 파일 제거 |

### Module:  MapDataManagement.py
|메서드|입력 인자|입력 인자 타입|출력 인자|출력 인자 타입|기능|
|:--:|:--:|:--:|:--:|:--:|:--:|
| getListViewDataFormat | mapID_p, playerID_p, TimeUpload_p, mapName_p | str, str, str, str | str | str | 데이터를 입력받아 ListView에 맞는 DataFormat으로 변환 |
| getListViewData | data, dataEnum | str, list() | data | str | ListViewDataFormat을 입력받아 dataEnum에 따른 value추출 |
| genKey | _len | int | ret | str | _len에 따른 랜덤문자열 return |
| getKeyData | key, player_id | str, str | data | list() | Data Server에서 key값에 따른 데이터 추출 |
| convert_mapID_to_mapData | mapID | str | data | str | Data Server에서 mapID에 따른 mapData 변환 |
| upload | upload_data | dict() |  |  | dictionary를 Data Server에 업로드 |
| getSortedMapList | key, player_id | str, str | data | list() | Data Server가 온라인이면 key값에 따른 sort된 MapList변환 |
| convert_toModel | map_data | list() | data | QStringListModel() | mapList를 QStringListModel()로 변환 |
| convert_MaptoString | map | dict() | data | str | dictionary으로 이루어진 map을 ListViewDataFormat에 맞게 변환 |

## Folder: Map

### Class:  MapListButton.py
|메서드|입력 인자|입력 인자 타입|출력 인자|출력 인자 타입|기능|
|:--:|:--:|:--:|:--:|:--:|:--:|
| \_\_init\_\_ 생성자 | text, connectLayout, x, y, fontname, fontsize | str, QVBoxLayout() or QHBoxLayout(), int, int, str, str |  |  | QPushButton Initialization |
| buttonClicked |  |  |  |  | 클릭된 버튼에 따라서 Call Event Method |
| onNewClick |  |  |  |  | 새로운 pygame custom을 열고 클리어시 MapNameDialog으로 연결 |
| onRandomClick |  |  |  |  | 서버에 받아온 Map중 아무거나 선택해 pygame play |
| onBackClick |  |  |  |  | MainLayout을 GameMainLayout으로 변환 |
| onLeftMoveClick |  |  |  |  | 왼쪽 페이지로 이동하고 refresh ListViewData |
| onRightMoveClick |  |  |  |  | 오른쪽 페이지로 이동하고 refresh ListViewData |
| updatePage | toPageNumber | int |  |  | 올바르지 않은 페이지면 이동하지 않고 올바르면 이동 |

### Class:  MapListLayout.py
|메서드|입력 인자|입력 인자 타입|출력 인자|출력 인자 타입|기능|
|:--:|:--:|:--:|:--:|:--:|:--:|
| \_\_init\_\_ 생성자 | GMain | GameMain() |  |  | Layout Initialization<br>refresh ListViewData |
| initUI |  |  |  |  | 기본 UI 틀 작성/적용 |
| getSearchLayout |  |  | layout | QHBoxLayout() | Sort QLabel & Sort QComboBox & Search QLineEdit & Search QPushButton으로 구성된 layout return|
| getLVBLayout |  |  | layout | QHBoxLayout() | ListViewLayout과 ButtonListLayout를 합친 layout return |
| getListViewLayout |  |  | layout | QVBoxLayout() | ListView와 PageMoveLayout으로 이루어진 layout return |
| getPageMoveLayout |  |  | layout | QHBoxLayout() | LeftMove QPushButton, Page QLabel과 RightMove QPushButton으로 이루어진 layout return |
| getPage |  |  | data | int | 현재 페이지 return |
| getButtonListLayout |  |  | layout | QVBoxLayout() | New QPushButton, Random QPushButton, Back QPushButton으로 이루어진 layout return |
| getMainLayout |  |  | self.mainLayout | Unknown | mainLayout return |
| setStatus | msg | str |  |  | StatusBar message 설정 |
| processMapRawData | data, already_rawdata | Unknown, bool |  |  | raw MapData를 변환해 pygame에 실행가능한 data로 변환해서 게임을 실행 |
| changeListViewData |  |  |  |  | Data Server가 온라인이 아니면 작동하지 않는다<br>QComboBox에 따라 선택적으로 Sort하여 현재 페이지에 맞는 ListViewData설정 |
| getSearchContent |  |  | self.searchLine.text() | str | 검색창 값 return |
| SearchFilter | mapList | list() | new_mapList | list() | getSearchContent()를 포함하는 map만으로 재구성된 mapList return |

### Class:  MapUploadConfirm.py
|메서드|입력 인자|입력 인자 타입|출력 인자|출력 인자 타입|기능|
|:--:|:--:|:--:|:--:|:--:|:--:|
| \_\_init\_\_ 생성자 | GMain | GameMain() |  |  |  |
| showMapNameDialog | map_data, connectedlayout | dict(), Unknown |  |  | map_data는 이미 검증된 Data이므로 map_name을 DiaLog로 최종결정해 upload() |
| upload | map_data, map_name, connectedLayout | dict(), str, Unknown |  |  | map_data, map_name과 기존의 Client ID, Player ID를 종합해 upload_data를 구성해 upload |

## Folder: Server-Internet

### Module: Internet.py
|메서드|입력 인자|입력 인자 타입|출력 인자|출력 인자 타입|기능|
|:--:|:--:|:--:|:--:|:--:|:--:|
| InternetConnected |  |  | bool | bool | 인터넷이 연결됐는지 확인 |
| getServerVersion |  |  | str | str | GitHub Version return |
| getDataServerOnline |  |  | bool | bool | Data Server이 온라인지 아닌지 return |

## Folder: Util

### Class:  MessageBox.py
|메서드|입력 인자|입력 인자 타입|출력 인자|출력 인자 타입|기능|
|:--:|:--:|:--:|:--:|:--:|:--:|
| \_\_init\_\_ 생성자 | text, windowtitle, fontname, fontsize | str, str, str, int |  |  | QMessageBox Initialization |
| \_\_str\_\_ |  |  | self | QMessabeBox() | 자기자신 객체 return |

## Folder: Server-Data Server

### Module:  server.py
|메서드|입력 인자|입력 인자 타입|출력 인자|출력 인자 타입|기능|
|:--:|:--:|:--:|:--:|:--:|:--:|
| readDB |  |  |  |  | 서버를 실행 시킬때 초기 todos, recentMapID, playerMapID, mapIDList를 읽어옴 |
| writeDB |  |  |  |  | 서버에 맵데이터가 upload 되었을 때 todos, recentMapID, playerMapID, mapIDList를 갱신함 |
| get | command | str | recentDict['mapData'] | dict() | mapID를 command인자로 받아들였을 때 그에 맞는 mapData로 변환함 |
| put | command=upload, data | str, dict() |  |  | mapID, playerID, TimeUpload, mapData, mapName을 입력받아 server에 upload시킴 |
| put | command=myMap, data | str, dict() | playerMapID[playerID][::-1] | list() | 자신의 clientID와 일치하는 playerID를 가진 mapData를 가져오는 기능 |
| put | command=recentMap | str | recentMapID[::-1] | list() | 최근에 제작된 맵을 가져옴 |

## Folder: PyGame

### Class:  gameMain.py
|메서드|입력 인자|입력 인자 타입|출력 인자|출력 인자 타입|기능|
|:--:|:--:|:--:|:--:|:--:|:--:|
| \_\_init\_\_ 생성자 | mapData | list() |  |  | pygame을 초기화시키고 mapData에 데이터가 들어있지 않은 경우 초기화 시키는 기능 |
| startgame | test | bool |  |  | Finding Star의 게임을 실행시키는 기능 <br> 게임 이벤트루프를 실행시킴 |
| startcustom |  |  |  |  | Finding Star의 커스텀을 실행시키는 기능 <br> 커스텀 이벤트루프를 실행시킴 |
| endgame |  |  |  |  | pygame을 안전하게 종료시키는 기능 |

### Module:  gameEventManagement.py
|메서드|입력 인자|입력 인자 타입|출력 인자|출력 인자 타입|기능|
|:--:|:--:|:--:|:--:|:--:|:--:|
| gameKeyBoardEvent | self | Game | True, False | bool | 키보드를 이용해서 플레이어를 x축으로 움직이게 함 |
| getHixBox | self | Game | hit_list | dict() | 현재 플레이어가 어떤 블럭에 닿았는지를 조사하는 기능 |
| moving | self | Game |  |  | 자동적으로 플레이어를 y축으로 움직이게 함 |
| init_moving | self | Game |  |  | 플레이어의 gravity, speed, vel_y, 초기 위치를 초기화시키는 기능 |
| checkIn | self, y, x, compare | Game, int, int, list() | self.mapData[(self.py+y)//SIZE][(self.px+x)//SIZE] in compare | bool | 플레이어를 기준으로 (x, y) 방향에 블럭이 있는지를 조사한 데이터를 반환 |
| gameHitEvent | self, hit_list | Game, dict() | True | bool | 플레이어가 블럭에 부딪혔을 시 어떻게 튕기는지 기술함 <br> 가시에 닿았을 경우 플레이어의 좌표와 맵이 초기화 <br> 별에 닿았을 경우 별을 없애고 별이 하나도 없을 경우 게임 종료 <br> 블럭에 닿았을 경우 튕기거나 gravity와 speed를 변화시키는 기능 |
| init_game | self, mapData, test | Game, list(), bool |  |  | pygame을 초기화시키고 화면크기와 제목을 설정함 |
| makeBlock | self | Game |  |  | 충돌을 감지하기 위해 블럭들을 convert_alpha()시킴 |

### Module:  gameDraw.py
|메서드|입력 인자|입력 인자 타입|출력 인자|출력 인자 타입|기능|
|:--:|:--:|:--:|:--:|:--:|:--:|
| drawBackground | self | Game |  |  | 게임 화면을 흰색으로 채움 |
| drawLine | self, isgame | Game, bool |  |  | 커스텀인 경우 한칸당 20*20의 격자를 생성시킴 |
| drawBlock | self, isgame | Game, bool |  |  | 게임 및 커스텀 화면에 블럭들을 그림 |
| drawPicture | self, isgame | Game, bool |  |  | drawBackground, drawLine, drawBlock method들을 실행시키고 fps에 맞춰 화면을 update시킴 |

### Module:  customEventManagement.py
|메서드|입력 인자|입력 인자 타입|출력 인자|출력 인자 타입|기능|
|:--:|:--:|:--:|:--:|:--:|:--:|
| init_custom | self, mapData | Game, list() |  |  | 커스텀 화면크기와 제목을 설정함 |
| customKeyBoardEvent | self | Game | True | bool | 커스텀의 마우스, 키보드 이벤트루프를 진행함 <br> 마우스 클릭시 블럭을 설치함 <br> 키보드 클릭시 설치할 블럭을 설정함 |

## __Other__

### Class:  Font.py
|메서드|입력 인자|입력 인자 타입|출력 인자|출력 인자 타입|기능|
|:--:|:--:|:--:|:--:|:--:|:--:|
| \_\_init\_\_ 생성자 | font, size | str, int |  |  | QFont Initialization |
| getFont |  |  | self.font | QFont() | font return |
| setBold | bool | bool |  |  | Font Bold 설정 |

### OPTION: options.py
|Attribute|기능|
|:--:|:--:|
| GAME_SIZE | Game Screen SIZE |
| GAME_TITLE | Game 제목 |
| blockList | 블럭 리스트 |
| CLIENT_ID_KEY | Client ID |
| VERSION | 버전 |
| GAME_SPEED | 게임 속도(배수) |
| SERVER_DISCONNECTED | 서버 연결 종료 메시지 |
| DATA_SERVER_IP | Data Server IP |

