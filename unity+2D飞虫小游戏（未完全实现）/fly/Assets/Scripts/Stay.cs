using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Stay : MonoBehaviour
{
    public int flyCount = 0;
    // Start is called before the first frame update
    void Start()
    {

    }

    // Update is called once per frame
    void Update()
    {
        
    }

    private void OnCollisionEnter2D(Collision2D other)
    {
        if(other.gameObject.CompareTag("fly"))
        {
            flyCount++;
            if(flyCount == 3)
            {
                GameOver();
            }
        }
    }

    void GameOver()
    {
        
    }
}
