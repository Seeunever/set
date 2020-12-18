using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class HouseFly : MonoBehaviour
{   
    // Start is called before the first frame update
    private bool canBeKilled = true;
    private float m_speed = 0.3f;

    public float moveFactor = 4;

    private float rx;
    private float faceTo;
    public bool isGameOver = false;
    public int flyCount = 0;

    // Start is called before the first frame update
    void Start()
    {
        transform.Rotate(0,0,180);
        SetBeginFaceTo();
    }

    // Update is called once per frame
    void Update()
    {
        UpdateMove();    
    }

    void SetBeginFaceTo()
    {
        faceTo = Random.Range(-1f,1f);
    }
    void UpdateMove()
    {
        moveFactor = Random.Range(2f,5f);
        if(this.transform.position.y>-1)
        {
            if (faceTo > 0)
            {
                rx = Mathf.Sin(Time.time)*Time.deltaTime*moveFactor;
            }
            else
            {
                rx = -Mathf.Sin(Time.time)*Time.deltaTime*moveFactor;
            }
            transform.Translate(new Vector3(rx,m_speed*Time.deltaTime,0));

            if (transform.position.x < -4 || transform.position.x > 4)
            {
                transform.Translate(new Vector3(-rx,m_speed*Time.deltaTime,0));
            }
        }
        else
        {
            canBeKilled = false;
            MoveToCake();
        }
    }

    void MoveToCake()
    {
        Vector3 stayPoint1 = new Vector3(0,-2,0);
        // Vector3 stayPoint2 = new Vector3(-2,-4,0);
        // Vector3 stayPoint3 = new Vector3(2,-4,0);
        // Vector3 currentPosition = this.transform.position;

        transform.position = Vector3.MoveTowards(this.transform.position,stayPoint1,Time.deltaTime*2);
        // flyCount++;
        // if (flyCount == 0)
        // {
        //     transform.position = Vector3.MoveTowards(transform.position,stayPoint1,Time.deltaTime*2);
        //     flyCount = 1;
        //     return;
        // }
        // else if(flyCount == 1)
        // {
        //     transform.position = Vector3.MoveTowards(transform.position,stayPoint2,Time.deltaTime*2);
        //     flyCount = 2;
        //     return;
        // }
        // else if(flyCount == 2)
        // {
        //     transform.position = Vector3.MoveTowards(transform.position,stayPoint3,Time.deltaTime*2);
        //     flyCount = 3;
        //     return;
        // }
        // else if(flyCount == 3)
        // {
        //     GameOver();
        // }
    }


    void GameOver()
    {
        isGameOver = true;
    }
}
