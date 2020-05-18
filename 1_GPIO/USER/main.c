#include "main.h"
#include "delay.h"
//led GPIOB GPIOB
//key PA0 HIGH PC13 PH2 PH3 GND
static u8 keyReleased = 1;
void init()
{
	
	HAL_Init();
	Stm32_Clock_Init(360,25,2,8);
	delay_init(180);

	__HAL_RCC_GPIOA_CLK_ENABLE();
	__HAL_RCC_GPIOB_CLK_ENABLE();
	__HAL_RCC_GPIOH_CLK_ENABLE();
	__HAL_RCC_GPIOC_CLK_ENABLE();

	GPIO_InitTypeDef GPIOIniture;
	GPIOIniture.Pin = GPIO_PIN_0|GPIO_PIN_1;
	GPIOIniture.Mode = GPIO_MODE_OUTPUT_PP;
	GPIOIniture.Speed = GPIO_SPEED_HIGH;
	HAL_GPIO_Init(GPIOB,&GPIOIniture);

	GPIOIniture.Pin = GPIO_PIN_0;
	GPIOIniture.Mode = GPIO_MODE_INPUT;
	GPIOIniture.Pull = GPIO_PULLDOWN;
	GPIOIniture.Speed = GPIO_SPEED_HIGH;
	HAL_GPIO_Init(GPIOA,&GPIOIniture);

	GPIOIniture.Pin = GPIO_PIN_3|GPIO_PIN_2;
	GPIOIniture.Mode = GPIO_MODE_INPUT;
	GPIOIniture.Pull = GPIO_PULLUP;
	GPIOIniture.Speed = GPIO_SPEED_HIGH;
	HAL_GPIO_Init(GPIOH,&GPIOIniture);

	GPIOIniture.Pin = GPIO_PIN_13;
	HAL_GPIO_Init(GPIOC,&GPIOIniture);
}
void LedReSet()
{
	HAL_GPIO_WritePin(GPIOB,GPIO_PIN_0|GPIO_PIN_1,GPIO_PIN_SET);
}

//DS0 接 PB1，DS1 接 PB0。

uint8_t keyScaner()
{
	if(HAL_GPIO_ReadPin(GPIOA,GPIO_PIN_0) == 1)
		return 1;
	else if(HAL_GPIO_ReadPin(GPIOC,GPIO_PIN_13) == 0)
		return 2;
	else if(HAL_GPIO_ReadPin(GPIOH,GPIO_PIN_2) == 0)
		return 3;
	else if(HAL_GPIO_ReadPin(GPIOH,GPIO_PIN_3) == 0)
		return 4;
	else
		return 0;
}
void Key(u8 mood)
{
	if(mood == 1)
		keyReleased = 1;
	if(keyScaner()&&keyReleased)
		{
			keyReleased = 0;
			
			delay_ms(10);
			switch (keyScaner())
			{
			case 1:
				HAL_GPIO_WritePin(GPIOB,GPIO_PIN_0,GPIO_PIN_SET);
				delay_ms(300);
				HAL_GPIO_WritePin(GPIOB,GPIO_PIN_0,GPIO_PIN_RESET);
				delay_ms(300);
				HAL_GPIO_WritePin(GPIOB,GPIO_PIN_0,GPIO_PIN_SET);
				HAL_GPIO_WritePin(GPIOB,GPIO_PIN_1,GPIO_PIN_RESET);//1 dam
				break;
			case 2:
				HAL_GPIO_WritePin(GPIOB,GPIO_PIN_1,GPIO_PIN_RESET);//0 light
				HAL_GPIO_WritePin(GPIOB,GPIO_PIN_0,GPIO_PIN_SET);//1 dam
				break;			
			case 3:
				HAL_GPIO_WritePin(GPIOB,GPIO_PIN_1,GPIO_PIN_RESET);//0 light
				HAL_GPIO_WritePin(GPIOB,GPIO_PIN_0,GPIO_PIN_RESET);//1 light
				break;	
			case 4:
				HAL_GPIO_WritePin(GPIOB,GPIO_PIN_1,GPIO_PIN_SET);//0 dam
				HAL_GPIO_WritePin(GPIOB,GPIO_PIN_0,GPIO_PIN_SET);//1 dam
				break;
			default:
				break;
			}
		}
		else if(keyScaner() == 0&& keyReleased == 0)
		{
			keyReleased = 1;
		}
}

int main(void)
{
	
	init();
	LedReSet();
	while (1)
	{
		Key(1);
		
	}
}

