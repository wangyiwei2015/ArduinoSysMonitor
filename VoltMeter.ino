#define DISPLAY_PIN 5
#define SET_PIN 2
#define FUNC_PIN 3
#define MODE_NUM 3//模式的数量

int data_select = 0;
int indata = 0;
int operating_mode = 1;
float temperature = 0;//模式1——显示室内温度
int cpu_usage = 0;//模式2——显示cpu使用率
int memory_usage = 0;//模式3——显示内存使用率
_Bool change_mode = false;//记录是否需要改变模式
_Bool change_setting = false;//记录是否需要改变设置
_Bool debounce = false;

void setup() {
  Serial.begin(115200);
  Serial.println("Initiating System...");
  
  pinMode(DISPLAY_PIN,OUTPUT);
  pinMode(SET_PIN,INPUT_PULLUP);
  pinMode(FUNC_PIN,INPUT_PULLUP);

  attachInterrupt( digitalPinToInterrupt(SET_PIN), onSetPushed, FALLING);
  attachInterrupt( digitalPinToInterrupt(FUNC_PIN), onFuncPushed, FALLING);

  //电压表初始化
  float i;
  for(i=0;i<5;i=i+0.1){
    displayVoltage(i);
    delay(10);
  }
  for(i=5;i>0;i=i-0.1){
    displayVoltage(i);
    delay(10);
  }
  Serial.println("Initialization Done!");
}

//主循环
void loop() {
  readData();//读取电脑发送的数据
  changeDisplay();
  if(change_mode == true)changeMode();//改变模式
  if(change_setting == true)changeSetting();//改变设置
}

//处理SET按键被按下的事件
void onSetPushed()
{
  change_setting = true;
}

//处理FUNC按键被按下的事件
void onFuncPushed()
{
  change_mode = true;
}

//将数据输出
void displayVoltage(float volt){
  analogWrite(DISPLAY_PIN,int(volt/5.0*255));
}

//读取串口的信息
void readData(){
  if(!Serial.available())return;
  if(Serial.read() == 'G'){
    Serial.println("Massage received!");
    data_select = Serial.parseInt();
    indata = Serial.parseInt();
    switch(data_select){
      case 1:{
        temperature = indata;
        break;
      }
      case 2:{
        cpu_usage= indata;
        break;
      }
      case 3:{
        memory_usage= indata;
        break;
      }
      default:{
        break;
      }
    }
    Serial.print("data_select:");
    Serial.println(data_select);
    Serial.print("indata:");
    Serial.println(indata);
  }
}

//模式切换
void changeMode(){
  if(debounce == true)return;
  debounce = true;
  Serial.print("Mode changed to ");
  if(operating_mode < MODE_NUM){
    operating_mode++;
  }
  else
  {
    operating_mode = 1;
  }
  Serial.println(operating_mode);
  delay(200);
  change_mode = false;
  debounce = false;
}

//改变设置
void changeSetting(){
  if(debounce == true)return;
  debounce = true;
  //未定内容
  Serial.println("Setting changed");
  delay(200);
  change_setting = false;
  debounce = false;
}


//改变显示内容
void changeDisplay(){
  switch(operating_mode){
    case 1:{
      displayVoltage(temperature/100.0*5);
      break;
    }
    case 2:{
      displayVoltage(cpu_usage/100.0*5);
      break;
    }
    case 3:{
      displayVoltage(memory_usage/100.0*5);
      break;
    }
    default:{
      break;
    }
  }
}
