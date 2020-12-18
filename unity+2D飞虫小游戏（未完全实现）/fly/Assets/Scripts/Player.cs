using System.Collections;
using System.Collections.Generic;
using UnityEngine;


public class Player : MonoBehaviour
{
    public GameObject a;
    public List<GameObject> _flys =  new List<GameObject>();
    public float m_speed = 1;

    public bool isGameOver;

    // Start is called before the first frame update
    void Start()
    {
        // isGameOver = transform.Find("common").gameObject.GetComponent<Common>().isGameOver;
    }

    // Update is called once per frame
    void Update()
    {
        UpdateMove(); 
        KillFly();   
    }

    void UpdateMove()
    {
        if (isGameOver == false)
        {
            float rx = Mathf.Sin(Time.time)*Time.deltaTime*3;
            transform.Translate(new Vector3(rx,0,0)*4);
            if(this.transform.position.x > 3.5f || this.transform.position.x <-3.5f)
            {
                transform.Translate(new Vector3(-rx,0,0)*4);
            }
        }

    }

public GameObject[] targetArr;
private List<float> KnifeList;
private Dictionary<float, GameObject> knifeDic;
    void KillFly()
    {
        targetArr = GameObject.FindGameObjectsWithTag("fly");
        if(Input.GetKeyDown(KeyCode.R))
        {
            for (int i = 0; i < targetArr.Length; i++)
            {   
                if(Mathf.Abs(targetArr[i].transform.position.x-this.transform.position.x)<=1)
                {
                    float dis = Vector3.Distance(targetArr[i].transform.position, this.transform.localPosition);
                    knifeDic.Add(dis, targetArr[i].gameObject);
                    Debug.Log(dis);
                    if (!KnifeList.Contains(dis))
                    {
                        KnifeList.Add(dis);
                    }
                }    
            }
            KnifeList.Sort();//对距离进行排序
            Debug.Log("***"+KnifeList[0]);
            GameObject obj;
            knifeDic.TryGetValue(KnifeList[0],out obj);//获取距离最近的对象
            Debug.Log(obj.name);
        }
    }
}
