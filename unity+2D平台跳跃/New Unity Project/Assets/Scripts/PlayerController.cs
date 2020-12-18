using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class PlayerController : MonoBehaviour
{
    // Start is called before the first frame update
    Rigidbody2D rb;
    Animator anim;

    public bool playerDead;
    public float speed;
    float xVelocity;

    public float checkRadius;

    public LayerMask platform;
    public GameObject groundCheck;
    public bool isOnGround;
    void Start()
    {
        rb = GetComponent<Rigidbody2D>();
        anim = GetComponent<Animator>();
    }

    // Update is called once per frame
    void Update()
    {
        isOnGround = Physics2D.OverlapCircle(groundCheck.transform.position,checkRadius,platform);
        anim.SetBool("isOnGround",isOnGround);
        Movement();
    }

    void Movement()
    {
        xVelocity = Input.GetAxisRaw("Horizontal");
        rb.velocity = new Vector2(xVelocity*speed,rb.velocity.y);
        anim.SetFloat("speed",Mathf.Abs(rb.velocity.x));
        if (xVelocity!=0)
        {
            transform.localScale = new Vector3(xVelocity,1,1);
        }
    }


    private void OnCollisionEnter2D(Collision2D other)
    {
        if(other.gameObject.CompareTag("Jump"))
        {
            rb.velocity = new Vector2(rb.velocity.x,10f);
        }
    }
    private void OnTriggerEnter2D(Collider2D other)
    {
        if (other.CompareTag("spike"))
        {
            anim.SetTrigger("dead");
        }
    }

    public void OnPlayerDead()
    {
        playerDead = true;
    }
    private void OnDrawGizmosSelected()
    {
        Gizmos.color = Color.blue;
        Gizmos.DrawWireSphere(groundCheck.transform.position,checkRadius);
    }
}
