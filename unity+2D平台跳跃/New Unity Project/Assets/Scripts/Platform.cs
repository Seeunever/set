using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Platform : MonoBehaviour
{
    // Start is called before the first frame update
    Vector3 movement;
    public float speed;
    
    GameObject topLine;
    void Start()
    {
        topLine = GameObject.Find("TopLine");
        movement.y = speed;
    }

    // Update is called once per frame
    void Update()
    {
        MovePlatform();
    }

    void MovePlatform()
    {
        transform.position += movement * Time.deltaTime;
        
        if (transform.position.y >= topLine.transform.position.y)
        {
            Destroy(gameObject);
        }
    }
}
